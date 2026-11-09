#!/usr/bin/env python3
"""Optional Arabic prosody check powered by separately installed pyarud."""
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Arabic spot optional prosody tool")
    parser.add_argument("--sadr", required=True, help="First half of the Arabic verse")
    parser.add_argument("--ajuz", required=True, help="Second half of the Arabic verse")
    args = parser.parse_args()
    try:
        from pyarud import analyze_verse, format_verse_report
    except ImportError:
        print("Missing optional dependency: run 'python3 -m pip install pyarud' first.", file=sys.stderr)
        return 2
    try:
        result = analyze_verse(args.sadr, args.ajuz)
        print(format_verse_report(result))
    except Exception as exc:
        print(f"Prosody engine error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
