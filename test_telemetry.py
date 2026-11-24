import unittest
from telemetry import depth_status


class TestDepthStatus(unittest.TestCase):

    def test_no_data(self):
        self.assertEqual(depth_status(None), "NO DATA")

    def test_live(self):
        self.assertEqual(depth_status(1.9), "LIVE")

    def test_stale_at_two_seconds(self):
        self.assertEqual(depth_status(2.0), "STALE")

    def test_stale_at_three_seconds(self):
        self.assertEqual(depth_status(3.0), "STALE")


if __name__ == "__main__":
    unittest.main()