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
  start - 12  dk-odds closes.yml, once per cluster of NBA/NFL/soccer starts not already covered by a
            collector call: the free closing snapshots (closing.py: ESPN + Action Network, no key,
            no credits). Start times come from ESPN's public scoreboards (same leagues as closing.py),
            with the published screens as a fallback. Jake chose this fix on 9 Nov (TEST_PLAN R3:
            GitHub's 15-minute cron gave closes for only 13 of 62 games on 7-8 Nov).
  OPS_JOBS  every free dk-odds job that used to rely on GitHub's cron (Jake, 9 Nov: none of dk-odds'
            scheduled runs fired from 3:43 am to 4:25 pm ET): box scores 5:20, lab 6:10 and 2:35, the
            NBA full-board screen 10:40 and 4:20, the NFL/soccer screen (6:45 Sat/Sun, 10:30 Sun,
            10:40 Tue/Wed, 4:15 Sun/Mon/Thu) and the 6:40 pm late-news re-screen. Their own crons stay
            as backups; every one of them is safe to run twice.

It never calls the Odds API itself and needs no API key. Dispatching dk-odds needs the
DK_ODDS_DISPATCH secret: a fine-grained token with Actions read/write on dk-odds only.
Without it, the ev-data refreshes still run and the dk-odds jobs are logged as skipped.

What it did is recorded in clock/<ET date>.json, so a restarted clock never repeats a job.
A run stops before GitHub's 6-hour limit and dispatches a fresh copy of itself. With --chain (what
clock.yml runs) it never stops for the night: it sleeps through to the next day's first job and keeps
handing over, so the day no longer depends on one of GitHub's cron starts landing (on 9 Nov none of
the five did). The crons in clock.yml are now only backups to restart a broken chain.

Usage: python3 -I pipeline/clock.py [--once] [--dry-run] [--chain]
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
FREE_LEAD_MIN = 12        # fire the free closes this long before the first start: lands ~10-12 min out (a "tight" close)
FREE_REACH_MIN = 20       # starts up to this long after the fire share the call (closing.py's window is 25)
COLLECTOR_REACH_MIN = 20  # a collector call only counts as covering starts this close to its fire time
SCOREBOARD_TTL = dt.timedelta(minutes=30)
SCOREBOARD_RETRY = dt.timedelta(minutes=5)  # after a failed fetch
SCOREBOARDS = {  # sport -> ESPN (sport, league) pairs; the same leagues closing.py snapshots
    "nba": [("basketball", "nba")],
    "nfl": [("football", "nfl")],
    "soccer": [("soccer", "eng.1"), ("soccer", "uefa.champions"), ("soccer", "esp.1"), ("soccer", "ger.1"),
               ("soccer", "ita.1")],
}
SITE = "https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard?dates={d}"
HANDOVER_TRIES = 3        # a failed hand-over dispatch is retried, 30 s apart, before giving up to the crons
DAY_JOBS = [  # (key, ET time, action)
    ("board_1405", (14, 5), "board"),
    ("auto_1425", (14, 25), "auto"),
    ("board_1445", (14, 45), "board"),
    ("board_1615", (16, 15), "board"),
]
ALL = (0, 1, 2, 3, 4, 5, 6)   # weekday() numbers, Monday = 0
SAT_SUN, SUN, TUE_WED, SUN_MON_THU = (5, 6), (6,), (1, 2), (6, 0, 3)
OPS_JOBS = [  # (key, ET time, action, weekdays, minutes it is still worth firing late); all free, no credits
    ("box_0520", (5, 20), "boxscores", ALL, 120),    # ev-data: yesterday's box scores (the lab grades from them)
    ("lab_0610", (6, 10), "lab", ALL, 240),
    ("mscreen_0645", (6, 45), "mscreen", SAT_SUN, 90),   # soccer, before the 7:59 am run
    ("mscreen_1030", (10, 30), "mscreen", SUN, 55),       # NFL, before the 11:29 am run
    ("escreen_1040", (10, 40), "escreen", ALL, 45),       # NBA full board, before the 11:29 am run
    ("mscreen_1040", (10, 40), "mscreen", TUE_WED, 45),   # Champions League
    ("lab_1435", (14, 35), "lab", ALL, 240),
    ("mscreen_1615", (16, 15), "mscreen", SUN_MON_THU, 25),  # NFL night games, for the 4:45 pm run
    ("escreen_1620", (16, 20), "escreen", ALL, 20),        # after the 4:15 pm board, for the 4:45 pm run
    ("news_1840", (18, 40), "latenews", ALL, 15),          # NBA nights only (see plan)
]
ACTIONS = {  # action -> (repo, workflow file, inputs, token env var)
    "board": ("jdarby00/ev-data", "nba.yml", {"boxscores": "true"}, "GITHUB_TOKEN"),
    "auto": ("jdarby00/dk-odds", "auto.yml", {}, "DK_ODDS_DISPATCH"),
    "close": ("jdarby00/dk-odds", "odds.yml", {}, "DK_ODDS_DISPATCH"),
    "freeclose": ("jdarby00/dk-odds", "closes.yml", {}, "DK_ODDS_DISPATCH"),
    "boxscores": ("jdarby00/ev-data", "nba.yml", {"boxscores": "true"}, "GITHUB_TOKEN"),
    "lab": ("jdarby00/dk-odds", "lab.yml", {}, "DK_ODDS_DISPATCH"),
    "escreen": ("jdarby00/dk-odds", "espn-screen.yml", {}, "DK_ODDS_DISPATCH"),
    "mscreen": ("jdarby00/dk-odds", "market-screen.yml", {}, "DK_ODDS_DISPATCH"),
    # late-news re-screens for free and may price up to 3 flagged spreads (1 credit each); autorequest skips
    # game-markets already requested today, so a second run (its own cron firing late) adds no repeat credits.
    "latenews": ("jdarby00/dk-odds", "late-news.yml", {}, "DK_ODDS_DISPATCH"),
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


def scoreboard_starts(day, get=None):
    """Start times (aware UTC) of today's not-yet-started NBA, NFL and soccer games from ESPN's public
    scoreboards. Returns (starts, ok): ok is False if any scoreboard failed, so the caller keeps its cache."""
    if get is None:
        from common import get_json

        def get(url):  # one quick try: a slow ESPN must never hold up due dispatches
            return get_json(url, tries=1, timeout=10)
    d = day.strftime("%Y%m%d")
    out, ok = [], True
    for pairs in SCOREBOARDS.values():
        for sport, league in pairs:
            sb = get(SITE.format(sport=sport, league=league, d=d))
            if sb is None:
                ok = False
                continue
            for ev in sb.get("events", []):
                state = ((ev.get("status") or {}).get("type") or {}).get("state")
                if state not in (None, "pre") or not ev.get("date"):
                    continue
                try:
                    out.append(parse_utc(ev["date"]))
                except ValueError:
                    continue
    return sorted(set(out)), ok


def screen_starts(root, day):
    """Fallback start times from the published NFL and soccer screens (NBA comes from the slate)."""
    out = []
    for rel in (f"board/nfl/{day.isoformat()}-screen.json", f"board/soccer/{day.isoformat()}-screen.json"):
        for g in (read_json(os.path.join(root, rel)) or {}).get("games", []):
            if g.get("state") in (None, "pre") and g.get("start_utc"):
                try:
                    out.append(parse_utc(g["start_utc"]))
                except ValueError:
                    pass
    return out


def ops_jobs(now, day, nba_tips, done):
    """The free dk-odds/ev-data jobs due today (OPS_JOBS), fired late only inside each job's window."""
    jobs = []
    for key, (h, m), action, days, late_min in OPS_JOBS:
        if key in done or day.weekday() not in days:
            continue
        if action == "latenews" and not nba_tips:
            continue  # the late-news re-screen is for NBA nights
        at = dt.datetime.combine(day, dt.time(h, m), ET).astimezone(UTC)
        if now <= at + dt.timedelta(minutes=late_min):
            jobs.append((at, key, action, []))
    return jobs


def plan(now, day, slate, prices, done, starts=()):
    """Jobs still to fire today: a sorted list of (fire_at UTC, key, action, covers).
    starts: every NBA/NFL/soccer start time today (for the free closes); tips a collector call covers are skipped."""
    nba_tips = slate_tips(slate)
    jobs = ops_jobs(now, day, nba_tips, done)
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
    collector = {iso(t) for f, _, a, cov in jobs if a == "close" for t in cov
                 if t <= f + dt.timedelta(minutes=COLLECTOR_REACH_MIN)}
    collector |= {k.split(":", 1)[1] for k in done if k.startswith("close:")}
    collector -= {k.split(":", 1)[1] for k in done if k.startswith("closefail:")}  # collector call gave up
    free = sorted({t for t in starts if iso(t) not in collector and f"fclose:{iso(t)}" not in done
                   and t - now > dt.timedelta(minutes=LAST_CALL_MIN)})
    while free:
        fire = free[0] - dt.timedelta(minutes=FREE_LEAD_MIN)
        cover = [t for t in free if t <= fire + dt.timedelta(minutes=FREE_REACH_MIN)]
        jobs.append((fire, f"fclose@{iso(fire)}", "freeclose", cover))
        free = [t for t in free if t not in cover]
    return sorted(jobs, key=lambda j: (j[0], j[1]))


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


def next_day_start(day):
    """00:01 ET on the day after `day`, in UTC."""
    return dt.datetime.combine(day + dt.timedelta(days=1), dt.time(0, 1), ET).astimezone(UTC)


def hand_over(state, state_path, day, now, dry_run, sleep):
    """Dispatch a fresh clock run (retried); log it. Returns True if a fresh run was started."""
    note = ""
    for i in range(HANDOVER_TRIES):
        ok, note = dispatch("self", dry_run)
        if ok:
            break
        if i + 1 < HANDOVER_TRIES:
            sleep(30)
    line = f"{iso(now)} hand-over to a fresh clock run: {note}"
    print(line)
    state["log"].append(line)
    if not dry_run:
        save_state(state_path, state, f"clock: hand-over {day.isoformat()}")
    return ok


def run(once=False, dry_run=False, now_fn=lambda: dt.datetime.now(UTC), sleep=time.sleep, get=None, chain=False):
    """Fire today's jobs. chain=True: also roll into the next ET day and keep handing over, never stopping."""
    started = now_fn()
    tries = {}
    board = {"at": None, "ok": True, "starts": [], "day": None}  # scoreboard cache
    day = state_path = state = None
    while True:
        now = now_fn()
        today = now.astimezone(ET).date()
        if day != today:
            if day is not None and not chain:
                print("past midnight ET; done for the day")
                return state
            day = today
            state_path = os.path.join(ROOT, "clock", f"{day.isoformat()}.json")
            os.makedirs(os.path.dirname(state_path), exist_ok=True)
            state = read_json(state_path) or {"date": day.isoformat(), "done": {}, "log": []}
            board = {"at": None, "ok": True, "starts": [], "day": day}
        if not dry_run:
            git("pull", "-q", "--rebase", "origin", "main")
        on_disk = read_json(state_path) or {}
        state["done"].update(on_disk.get("done", {}))  # jobs another clock run recorded
        slate = read_json(os.path.join(ROOT, "data", "nba", "slate", f"{day.isoformat()}.json"))
        prices = read_json(os.path.join(ROOT, "prices", f"{day.isoformat()}.json"))
        if board["at"] is None or now - board["at"] >= (SCOREBOARD_TTL if board["ok"] else SCOREBOARD_RETRY):
            fetched, ok = scoreboard_starts(day, get)
            board["starts"] = sorted(set(board["starts"]) | set(fetched))  # merge: a failed league never drops games
            board["at"], board["ok"] = now, ok
        starts = sorted(set(board["starts"]) | set(screen_starts(ROOT, day)) | set(slate_tips(slate)))
        jobs = plan(now, day, slate, prices, state["done"], starts)
        if not jobs and not chain:
            print("nothing left today")
            return state
        if jobs:
            fire, key, action, cover = jobs[0]
        else:  # chain: nothing left today; wake for tomorrow's plan
            fire, key, action, cover = next_day_start(day), "next day", None, []
        if action and fire <= now:
            ok, note = dispatch(action, dry_run)
            tries[key] = tries.get(key, 0) + 1
            line = f"{iso(now)} {key}: {note}"
            print(line)
            state["log"].append(line)
            if ok or note.startswith("skipped") or tries[key] >= 3:
                state["done"][key] = iso(now)
                for t in cover:
                    state["done"][f"{'fclose' if action == 'freeclose' else 'close'}:{iso(t)}"] = iso(now)
                    if action == "close" and not ok:
                        state["done"][f"closefail:{iso(t)}"] = iso(now)  # let the free closes cover it
            if not dry_run:
                save_state(state_path, state, f"clock: {key} {day.isoformat()}")
            if once:
                return state
            continue
        if once:
            return state
        if now >= started + RUN_BUDGET:
            hand_over(state, state_path, day, now, dry_run, sleep)
            return state
        nap = min((fire - now).total_seconds(), MAX_NAP, (started + RUN_BUDGET - now).total_seconds())
        print(f"{iso(now)} next: {key} at {iso(fire)}; sleeping {int(nap)} s")
        sleep(max(nap, 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true", help="fire anything due now, then stop")
    ap.add_argument("--dry-run", action="store_true", help="don't dispatch, commit or pull")
    ap.add_argument("--check-token", action="store_true", help="test DK_ODDS_DISPATCH with a no-op dk-odds job")
    ap.add_argument("--chain", action="store_true", help="never stop for the night: roll into the next day and hand over")
    args = ap.parse_args()
    if args.check_token:
        ok, note = dispatch("check")
        print(note)
        sys.exit(0 if ok else 1)
    run(once=args.once, dry_run=args.dry_run, chain=args.chain)


if __name__ == "__main__":
    main()
