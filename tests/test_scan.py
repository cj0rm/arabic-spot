"""Offline regression tests for the optional PyArud helper."""
import contextlib
import io
import sys
import types
import unittest
from unittest.mock import patch

from scripts import scan


class ScannerTests(unittest.TestCase):
    def test_calls_documented_pyarud_processor_api(self):
        calls = []
        fake = types.ModuleType("pyarud")

        class FakeProcessor:
            def analyze_verse(self, sadr, ajuz):
                calls.append((sadr, ajuz))
                return {"checked": True}

        fake.ArudhProcessor = FakeProcessor
        fake.format_verse_report = lambda result: "Verse report: " + str(result["checked"])
        stream = io.StringIO()
        with patch.dict(sys.modules, {"pyarud": fake}):
            with patch.object(sys, "argv", ["scan.py", "--sadr", "صدر", "--ajuz", "عجز"]):
                with contextlib.redirect_stdout(stream):
                    status = scan.main()
        self.assertEqual(status, 0)
        self.assertEqual(calls, [("صدر", "عجز")])
        self.assertIn("Verse report: True", stream.getvalue())

    def test_friendly_error_without_optional_pyarud(self):
        stream = io.StringIO()
        with patch.dict(sys.modules, {"pyarud": None}):
            with patch.object(sys, "argv", ["scan.py", "--sadr", "صدر", "--ajuz", "عجز"]):
                with contextlib.redirect_stderr(stream):
                    status = scan.main()
        self.assertEqual(status, 2)
        self.assertIn("pip install pyarud", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
