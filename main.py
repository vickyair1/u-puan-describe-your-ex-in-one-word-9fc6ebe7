"""Describe Your Ex in One Word — make.fun bounty entry.

Writes exactly one word to /output/entry.txt, byte-for-byte, with no
trailing newline. Deterministic: the same bytes on every run, no
randomness, no time, no network, standard library only.

The word: "Autocorrect" — the ex who kept rewriting everything you
said, so you were never allowed to mean what you meant.
"""

import os

def get_word():
    """Return the one-word entry.

    The word: "Autocorrect" — the ex who kept rewriting everything you
    said, so you were never allowed to mean what you meant.
    """
    return "Autocorrect"


def get_output_dir():
    """Return the directory the entry is written to.

    Honours MAKEFUN_OUTPUT_DIR when set (the kit harness may point the
    entry elsewhere); falls back to the bounty-standard /output.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


MAX_WORD_LENGTH = 20


def validate_word(word):
    """Check the entry is exactly one word within the cap, before writing.

    A valid entry is a single non-empty token with no whitespace and no
    more than MAX_WORD_LENGTH characters.
    """
    assert isinstance(word, str) and word, "entry word must be non-empty"
    assert not any(ch.isspace() for ch in word), "entry must be one word"
    assert len(word) <= MAX_WORD_LENGTH, (
        f"entry word {len(word)} chars exceeds cap of {MAX_WORD_LENGTH}"
    )
    return word


def main():
    word = validate_word(get_word())
    output_dir = get_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as f:
        f.write(word.encode("utf-8"))
    print(word)


if __name__ == "__main__":
    main()
