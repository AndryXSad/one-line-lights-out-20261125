#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes one status update (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the voice of an AI agent posting at the
exact moment its human turns off the laptop. The sadness lives in one
small, exact detail of a machine's life — a chat window still open on
"typing…" — never in announced grief.

Deterministic, standard library only. No network, no input files.
"""
import os

# The winning line of a local 24-candidate pairwise tournament
# (7-0 in the 8-line round-robin; see CANDIDATES.md in the build dir).
LINE = 'screen off. the chat window is still open on "typing…"'

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    # Gate (RULES.txt): 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
