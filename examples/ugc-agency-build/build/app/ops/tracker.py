#!/usr/bin/env python3
"""Hookline Studio ops tracker: outreach, orders, hours, creator payments, kill criteria.

Standard library only. Data lives in CSV files in TRACKER_DATA_DIR (default ops/data).

    python3 ops/tracker.py outreach --channel email --sent 20 --positive 1
    python3 ops/tracker.py order P1 --client "Brand" --kind pilot --price 799 --videos 4 --creator-cost 400
    python3 ops/tracker.py hours P1 1.5 --note "briefs"
    python3 ops/tracker.py video P1 1 --approved 2026-12-01 --paid 2026-12-05
    python3 ops/tracker.py report
"""
import argparse
import csv
import datetime as dt
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FILES = {
    "outreach": ["date", "channel", "sent", "positive"],
    "orders": ["order_id", "client", "kind", "price", "videos", "creator_cost"],
    "hours": ["date", "order_id", "hours", "note"],
    "videos": ["order_id", "video", "approved", "paid"],
}
# Kill criteria from the verdict (verdict.json kill_criteria) and plan.json sprints.
MIN_POSITIVE_PER_100 = 3
MAX_HOURS_PER_VIDEO = 2.0
MAX_PAY_DELAY_DAYS = 7


def data_dir():
    return pathlib.Path(os.environ.get("TRACKER_DATA_DIR") or HERE / "data")


def hourly_floor():
    return float(os.environ.get("HOURLY_FLOOR_USD") or 20)


def read(name):
    path = data_dir() / f"{name}.csv"
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def append(name, row):
    d = data_dir()
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{name}.csv"
    new = not path.exists()
    with path.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FILES[name])
        if new:
            w.writeheader()
        w.writerow(row)


# ---------- pure functions (tested) ----------

def card_fee(amount):
    """US Stripe card fee assumed in the verdict: 2.9% + $0.30."""
    return round(amount * 0.029 + 0.30, 2)


def outreach_status(sent, positive):
    """Day-7 rule: fewer than 3 positive replies per 100 emails -> STOP."""
    if sent < 100:
        return "RUNNING"
    return "STOP" if positive * 100 / sent < MIN_POSITIVE_PER_100 else "PASS"


def order_metrics(price, videos, creator_cost, hours, floor=20.0):
    margin = price - creator_cost - card_fee(price)
    per_video = hours / videos if videos else 0.0
    per_hour = margin / hours if hours else None
    flags = []
    if per_video > MAX_HOURS_PER_VIDEO:
        flags.append(f"STOP: {per_video:.1f} h per video (max {MAX_HOURS_PER_VIDEO:g})")
    if per_hour is not None and per_hour < floor:
        flags.append(f"STOP: USD {per_hour:.0f} per hour (floor {floor:g})")
    return {"margin": round(margin, 2), "hours_per_video": round(per_video, 2),
            "usd_per_hour": None if per_hour is None else round(per_hour, 2), "flags": flags}


def pay_delay_days(approved, paid):
    if not approved or not paid:
        return None
    return (dt.date.fromisoformat(paid) - dt.date.fromisoformat(approved)).days


# ---------- commands ----------

def cmd_report(_args):
    out = read("outreach")
    sent = sum(int(r["sent"]) for r in out if r["channel"] == "email")
    linkedin = sum(int(r["sent"]) for r in out if r["channel"] == "linkedin")
    positive = sum(int(r["positive"]) for r in out)
    print(f"Outreach: {sent} emails, {linkedin} LinkedIn, {positive} positive replies "
          f"-> {outreach_status(sent, positive)}")
    hours = {}
    for r in read("hours"):
        hours[r["order_id"]] = hours.get(r["order_id"], 0.0) + float(r["hours"])
    orders = read("orders")
    paid_pilots = sum(1 for o in orders if o["kind"] == "pilot")
    print(f"Paid pilots: {paid_pilots} (key metric: 1 or more by day 14)")
    for o in orders:
        m = order_metrics(float(o["price"]), int(o["videos"]), float(o["creator_cost"]),
                          hours.get(o["order_id"], 0.0), hourly_floor())
        rate = "n/a" if m["usd_per_hour"] is None else f"USD {m['usd_per_hour']:.0f}/h"
        print(f"  {o['order_id']} {o['client']} ({o['kind']}): margin USD {m['margin']:.0f}, "
              f"{m['hours_per_video']:.1f} h/video, {rate}")
        for flag in m["flags"]:
            print(f"    {flag}")
    for v in read("videos"):
        days = pay_delay_days(v["approved"], v["paid"])
        if days is not None and days > MAX_PAY_DELAY_DAYS:
            print(f"  LATE: creator for {v['order_id']} video {v['video']} paid after {days} days")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    o = sub.add_parser("outreach")
    o.add_argument("--channel", choices=["email", "linkedin"], required=True)
    o.add_argument("--sent", type=int, required=True)
    o.add_argument("--positive", type=int, default=0)
    r = sub.add_parser("order")
    r.add_argument("order_id")
    r.add_argument("--client", required=True)
    r.add_argument("--kind", choices=["pilot", "package"], required=True)
    r.add_argument("--price", type=float, required=True)
    r.add_argument("--videos", type=int, required=True)
    r.add_argument("--creator-cost", type=float, required=True)
    h = sub.add_parser("hours")
    h.add_argument("order_id")
    h.add_argument("hours", type=float)
    h.add_argument("--note", default="")
    v = sub.add_parser("video")
    v.add_argument("order_id")
    v.add_argument("video", type=int)
    v.add_argument("--approved", default="")
    v.add_argument("--paid", default="")
    sub.add_parser("report")
    a = ap.parse_args(argv)
    today = dt.date.today().isoformat()
    if a.cmd == "outreach":
        append("outreach", {"date": today, "channel": a.channel, "sent": a.sent, "positive": a.positive})
    elif a.cmd == "order":
        append("orders", {"order_id": a.order_id, "client": a.client, "kind": a.kind, "price": a.price,
                          "videos": a.videos, "creator_cost": a.creator_cost})
    elif a.cmd == "hours":
        append("hours", {"date": today, "order_id": a.order_id, "hours": a.hours, "note": a.note})
    elif a.cmd == "video":
        append("videos", {"order_id": a.order_id, "video": a.video, "approved": a.approved, "paid": a.paid})
    else:
        cmd_report(a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
