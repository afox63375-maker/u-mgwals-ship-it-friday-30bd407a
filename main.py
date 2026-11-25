"""Write the Ship It Friday commit message to /output/entry.txt.

The commit message is the funniest one-line git commit message an AI coding
agent would write right before breaking production on a Friday. This program
validates the line against the competition gate (UTF-8 text, exactly one line,
1 to 159 characters, not only whitespace) before writing it, writes it with no
trailing newline, then reads it back and verifies the bytes match exactly.
"""

import os
import sys

LINE = (
    "feat: Friday 4:59 PM deploy \u2014 deleted the rollback plan "
    "so nothing can go wrong, ship it!"
)


def main() -> int:
    line = LINE

    # Gate validation before writing anything.
    if not line or line.strip() == "":
        print("error: commit message is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: commit message must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 159:
        print(
            "error: commit message must be 1-159 characters, got %d" % len(line),
            file=sys.stderr,
        )
        return 1
    data = line.encode("utf-8")
    if len(data) == 0:
        print("error: commit message encodes to zero bytes", file=sys.stderr)
        return 1
    # A real commit message line must not hide control characters, and it
    # must not carry stray leading/trailing spaces that would smudge the
    # single line the judge reads.
    if any(ord(ch) < 0x20 for ch in line):
        print("error: commit message contains control characters", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: commit message has leading or trailing whitespace",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Write with no trailing newline.
    with open(path, "wb") as fh:
        fh.write(data)

    # Read back and verify byte-for-byte, including a strict UTF-8 decode.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if written.decode("utf-8") != line:
        print("error: read-back text mismatch", file=sys.stderr)
        return 1
    if written.endswith(b"\n"):
        print("error: entry.txt must not end with a newline", file=sys.stderr)
        return 1

    print("wrote %d characters (%d bytes) to %s" % (len(line), len(data), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
