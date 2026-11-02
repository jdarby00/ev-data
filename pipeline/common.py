"""Shared helpers: ESPN fetch, ET dates, file IO. Standard library only."""
import csv
import datetime as dt
import gzip
import json
import os
import time
import urllib.request
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
ESPN = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (ev-data pipeline)"}


def get_json(url, tries=4, timeout=30):
    """GET a JSON URL with retries. Returns None after the last failure."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # network errors are expected now and then
            print(f"  fetch failed ({i + 1}/{tries}): {url} :: {type(e).__name__}")
            time.sleep(2 + 3 * i)
    return None


def today_et():
    return dt.datetime.now(ET).date()


def to_et(iso_utc):
    """'2026-11-02T00:30Z' -> aware ET datetime."""
    s = iso_utc.replace("Z", "+00:00")
    if len(s) == 22 and s[16] == "+":  # ESPN sometimes omits seconds: 2026-11-02T00:30+00:00
        s = s[:16] + ":00" + s[16:]
    return dt.datetime.fromisoformat(s).astimezone(ET)


def path(*parts):
    p = os.path.join(ROOT, *parts)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def write_json(p, obj):
    with open(p, "w") as fh:
        json.dump(obj, fh, indent=1, sort_keys=False)
        fh.write("\n")


def read_csv(p):
    if not os.path.exists(p):
        return []
    opener = gzip.open if p.endswith(".gz") else open
    with opener(p, "rt", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(p, rows, cols):
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def num(x, default=0.0):
    """ESPN stat strings -> float ('+5' -> 5, '' -> default, '7-15' -> 7)."""
    if x is None or x == "" or x == "--":
        return default
    s = str(x)
    if "-" in s[1:]:
        s = s.split("-")[0] if not s.startswith("-") else "-" + s[1:].split("-")[0]
    try:
        return float(s)
    except ValueError:
        return default
