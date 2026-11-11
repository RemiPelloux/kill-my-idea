import contextlib
import io
import os
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "ops"))
import tracker  # noqa: E402


class PureFunctions(unittest.TestCase):
    def test_card_fee_matches_verdict_assumption(self):
        self.assertEqual(tracker.card_fee(1200), 35.10)

    def test_outreach_stop_under_3_positive_per_100(self):
        self.assertEqual(tracker.outreach_status(100, 2), "STOP")
        self.assertEqual(tracker.outreach_status(100, 3), "PASS")
        self.assertEqual(tracker.outreach_status(40, 0), "RUNNING")

    def test_flags_more_than_2_hours_per_video(self):
        m = tracker.order_metrics(799, 4, 400, 10)
        self.assertEqual(m["hours_per_video"], 2.5)
        self.assertTrue(any("h per video" in f for f in m["flags"]))

    def test_flags_hourly_rate_under_floor(self):
        m = tracker.order_metrics(799, 4, 700, 8, floor=20)  # margin ~$75 / 8 h
        self.assertTrue(any("per hour" in f for f in m["flags"]))

    def test_healthy_pilot_has_no_flags(self):
        m = tracker.order_metrics(799, 4, 400, 6)
        self.assertEqual(m["flags"], [])

    def test_pay_delay(self):
        self.assertEqual(tracker.pay_delay_days("2026-12-01", "2026-12-09"), 8)
        self.assertIsNone(tracker.pay_delay_days("2026-12-01", ""))


class Commands(unittest.TestCase):
    def test_round_trip_report(self):
        with tempfile.TemporaryDirectory() as d:
            os.environ["TRACKER_DATA_DIR"] = d
            try:
                tracker.main(["outreach", "--channel", "email", "--sent", "100", "--positive", "4"])
                tracker.main(["order", "P1", "--client", "Test", "--kind", "pilot", "--price", "799",
                              "--videos", "4", "--creator-cost", "400"])
                tracker.main(["hours", "P1", "6"])
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    tracker.main(["report"])
                out = buf.getvalue()
            finally:
                del os.environ["TRACKER_DATA_DIR"]
        self.assertIn("-> PASS", out)
        self.assertIn("Paid pilots: 1", out)
        self.assertIn("1.5 h/video", out)


if __name__ == "__main__":
    unittest.main()
