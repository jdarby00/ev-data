"""The clock: fires the day's timed jobs at the right minute, because GitHub's own cron
schedules run hours late or not at all (2 Nov: the 2:25 pm price request ran at 8:42 pm,
and none of the 28 evening collector slots produced a close snapshot).

One long-running job in this public repo (Actions minutes are free here) sleeps until each
job is due and dispatches it:

  14:05 ET  ev-data pipeline (fresh board before the price request)
  14:25 ET  dk-odds auto-request (lock prices for the necessary game-markets)
  14:45 ET  ev-data pipeline (the screener reads the fresh lock prices and logs shadow bets)
  16:15 ET  ev-data pipeline (fresh board and statuses before the 4:45 pm Claude run)
  tip - 12  dk-odds collector, once per cluster of tips (close snapshots, inside its
            30-minute close window; tips up to 28 minutes later share the same call)

It never calls the Odds API itself and needs no API key. Dispatching dk-odds needs the
DK_ODDS_DISPATCH secret: a fine-grained token with Actions read/write on dk-odds only.
Without it, the ev-data refreshes still run and the dk-odds jobs are logged as skipped.

What it did is recorded in clock/<ET date>.json, so a restarted clock never repeats a job.
A run stops before GitHub's 6-hour limit and dispatches a fresh copy of itself if jobs remain.

Usage: python3 -I pipeline/clock.py [--once] [--dry-run]
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ET, ROOT  # noqa: E402

UTC = dt.timezone.utc
CLOSE_LEAD_MIN = 12       # fire the collector this long before the earliest tip in a cluster
CLUSTER_MIN = 28          # later tips inside this span share the call (collector window is 30)
LAST_CALL_MIN = 3         # too close to the tip to bother
RUN_BUDGET = dt.timedelta(hours=5, minutes=35)  # GitHub kills jobs at 6 h
MAX_NAP = 600             # wake at least every 10 minutes to refresh the plan
DAY_JOBS = [  # (key, ET time, action)
    ("board_1405", (14, 5), "board"),
    ("auto_1425", (14, 25), "auto"),
    ("board_1445", (14, 45), "board"),
    ("board_1615", (16, 15), "board"),
]
ACTIONS = {  # action -> (repo, workflow file, inputs, token env var)
    "board": ("jdarby00/ev-data", "nba.yml", {"boxscores": "true"}, "GITHUB_TOKEN"),
    "auto": ("jdarby00/dk-odds", "auto.yml", {}, "DK_ODDS_DISPATCH"),
    "close": ("jdarby00/dk-odds", "odds.yml", {}, "DK_ODDS_DISPATCH"),
    "self": ("jdarby00/ev-data", "clock.yml", {}, "GITHUB_TOKEN"),
    # Token check: a dk-odds job that does nothing when its data is already there (no credits).
    "check": ("jdarby00/dk-odds", "fetch-espn.yml", {}, "DK_ODDS_DISPATCH"),
}


def parse_utc(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(UTC)


def iso(t):
    return t.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_json(p):
    try:
        with open(p) as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None


def slate_tips(slate):
    """Not-yet-final NBA tips from the ESPN slate, as aware UTC times."""
    out = []
    for g in (slate or {}).get("games", []):
        if g.get("state") == "post":
            continue
        try:
            t = dt.datetime.strptime(g["tip_et"], "%Y-%m-%d %H:%M").replace(tzinfo=ET)
        except (KeyError, ValueError):
            continue
        out.append(t.astimezone(UTC))
    return out


def price_tips(prices):
    """(tips still needing a close, tips that already have one) from a published prices file."""
    need, have = [], []
    for g in (prices or {}).get("groups", {}).values():
        if not g.get("commence_time"):
            continue
        t = parse_utc(g["commence_time"])
        closed = any(s.get("kind") == "close" or s.get("also_close") for s in g.get("snapshots", []))
        (have if closed else need).append(t)
    return need, have


def plan(now, day, slate, prices, done):
    """Jobs still to fire today: a sorted list of (fire_at UTC, key, action, covers)."""
    jobs = []
    nba_tips = slate_tips(slate)
    first_tip = min(nba_tips) if nba_tips else None
    if nba_tips:
        for key, (h, m), action in DAY_JOBS:
            if key in done:
                continue
            at = dt.datetime.combine(day, dt.time(h, m), ET).astimezone(UTC)
            # Late is still useful until the slate starts (board) or an hour before the last tip (auto).
            useful_until = first_tip if action == "board" else max(nba_tips) - dt.timedelta(minutes=60)
            if now < useful_until:
                jobs.append((at, key, action, []))
    need, have = price_tips(prices)
    if prices is None:  # nothing published yet: fall back to the NBA slate
        need = nba_tips
    have_keys = {iso(t) for t in have}
    tips = sorted({t for t in need if iso(t) not in have_keys and f"close:{iso(t)}" not in done
                   and t - now > dt.timedelta(minutes=LAST_CALL_MIN)})
    while tips:
        first = tips[0]
        fire = first - dt.timedelta(minutes=CLOSE_LEAD_MIN)
        cover = [t for t in tips if t <= fire + dt.timedelta(minutes=CLUSTER_MIN)]
        jobs.append((fire, f"close@{iso(fire)}", "close", cover))
        tips = [t for t in tips if t not in cover]
    return sorted(jobs, key=lambda j: j[0])


def dispatch(action, dry_run=False):
    """POST a workflow_dispatch. Returns (ok, note). Never prints a token."""
    repo, wf, inputs, env = ACTIONS[action]
    token = os.environ.get(env, "")
    if not token:
        return False, f"skipped: {env} not set"
    if dry_run:
        return True, f"dry run: would dispatch {repo} {wf}"
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/actions/workflows/{wf}/dispatches",
        data=json.dumps({"ref": "main", "inputs": inputs}).encode(), method="POST",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "ev-data-clock"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 204, f"dispatched {repo} {wf} (HTTP {r.status})"
    except urllib.error.HTTPError as e:
        return False, f"{repo} {wf} dispatch failed: HTTP {e.code}"
    except Exception as e:  # network trouble; try again next loop
        return False, f"{repo} {wf} dispatch failed: {type(e).__name__}"


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)


def save_state(path_, state, msg):
    with open(path_, "w") as fh:
        json.dump(state, fh, indent=1, sort_keys=True)
        fh.write("\n")
    git("add", os.path.relpath(path_, ROOT))
    if git("diff", "--cached", "--quiet").returncode == 0:
        return
    git("-c", "user.name=ev-data clock", "-c", "user.email=ev-data@users.noreply.github.com",
        "commit", "-q", "-m", msg)
    for _ in range(3):
        if git("pull", "-q", "--rebase", "origin", "main").returncode == 0 and git("push", "-q").returncode == 0:
            return
        time.sleep(5)
    print("  could not push clock state; it will be retried next save")


def run(once=False, dry_run=False, now_fn=lambda: dt.datetime.now(UTC), sleep=time.sleep):
    started = now_fn()
    day = started.astimezone(ET).date()
    state_path = os.path.join(ROOT, "clock", f"{day.isoformat()}.json")
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    tries = {}
    state = read_json(state_path) or {"date": day.isoformat(), "done": {}, "log": []}
    while True:
        if not dry_run:
            git("pull", "-q", "--rebase", "origin", "main")
        on_disk = read_json(state_path) or {}
        state["done"].update(on_disk.get("done", {}))  # jobs another clock run recorded
        slate = read_json(os.path.join(ROOT, "data", "nba", "slate", f"{day.isoformat()}.json"))
        prices = read_json(os.path.join(ROOT, "prices", f"{day.isoformat()}.json"))
        now = now_fn()
        if now.astimezone(ET).date() != day:
            print("past midnight ET; done for the day")
            return state
        jobs = plan(now, day, slate, prices, state["done"])
        if not jobs:
            print("nothing left today")
            return state
        fire, key, action, cover = jobs[0]
        if fire <= now:
            ok, note = dispatch(action, dry_run)
            tries[key] = tries.get(key, 0) + 1
            line = f"{iso(now)} {key}: {note}"
            print(line)
            state["log"].append(line)
            if ok or note.startswith("skipped") or tries[key] >= 3:
                state["done"][key] = iso(now)
                for t in cover:
                    state["done"][f"close:{iso(t)}"] = iso(now)
            if not dry_run:
                save_state(state_path, state, f"clock: {key} {day.isoformat()}")
            if once:
                return state
            continue
        if once:
            return state
        if now >= started + RUN_BUDGET:
            ok, note = dispatch("self", dry_run)
            line = f"{iso(now)} hand-over to a fresh clock run: {note}"
            print(line)
            state["log"].append(line)
            if not dry_run:
                save_state(state_path, state, f"clock: hand-over {day.isoformat()}")
            return state
        nap = min((fire - now).total_seconds(), MAX_NAP, (started + RUN_BUDGET - now).total_seconds())
        print(f"{iso(now)} next: {key} at {iso(fire)}; sleeping {int(nap)} s")
        sleep(max(nap, 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true", help="fire anything due now, then stop")
    ap.add_argument("--dry-run", action="store_true", help="don't dispatch, commit or pull")
    ap.add_argument("--check-token", action="store_true", help="test DK_ODDS_DISPATCH with a no-op dk-odds job")
    args = ap.parse_args()
    if args.check_token:
        ok, note = dispatch("check")
        print(note)
        sys.exit(0 if ok else 1)
    run(once=args.once, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
