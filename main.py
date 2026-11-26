"""Entry for make.fun's The Meeting That Should Have Been an Email bounty."""

import argparse
import os
import sys
from pathlib import Path

LINE = "Forty minutes to agree we need another meeting, twenty to agree the first one was unnecessary, and tomorrow's is to decide who gets to say that out loud."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate the entry length")
    args = parser.parse_args()

    if args.check:
        if not 1 <= len(LINE) <= 200:
            print("Entry length must be between 1 and 200 characters.", file=sys.stderr)
            return 1
        print("Entry length OK: {} characters".format(len(LINE)))
        return 0

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
    print(len(LINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
