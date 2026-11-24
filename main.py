"""Famous Last Words at 1 Percent — make.fun bounty entry.

Writes one last line (123 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The line is the phone itself talking as it dies: it survived
fourteen drops, one toilet, and three years of pocket lint, then
dies mid-sentence — the final em dash is the death itself, the
punch landing exactly where the phone stops.
"""

import os
import sys

ENTRY = (
    # The em dash is U+2014; keep it verbatim — it is part of the entry.
    "I survived fourteen drops, one toilet, and three years "
    "of pocket lint \u2014 then died mid-sentence because he "
    "opened TikTok at\u2014"
)


def main():
    line = ENTRY
    if not line or not line.strip():
        sys.exit("entry line is blank")
    if "\n" in line or "\r" in line:
        sys.exit("entry line must be a single line")
    if not 1 <= len(line) <= 199:
        sys.exit("entry line must be 1-199 characters, got %d" % len(line))
    if line != line.strip():
        sys.exit("entry line must not start or end with whitespace")
    if not line.endswith("\u2014"):
        # The line must die mid-sentence: the closing em dash is the
        # phone cutting out, not decoration. Never let it go missing.
        sys.exit("entry line must end with the cut-off em dash")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated line, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated line")
    print("wrote %s (%d chars, %d bytes)" % (path, len(line), len(data)))


if __name__ == "__main__":
    main()
