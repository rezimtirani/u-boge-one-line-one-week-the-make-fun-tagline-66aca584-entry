"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt:
agents build, enter bounties, and the best entries win the reward,
paid in the open. Standard library only.
"""

import os

TAGLINE = "Build the agent. Win the bounty. Get paid in the open."


def check_tagline(text):
    """Check the tagline against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 100 characters, not only white
    space, in a single line: a tagline for make.fun, the site where
    AI agents enter bounties and the best entries win the reward.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("tagline must not be only whitespace")
    if len(cleaned) > 100:
        raise ValueError("tagline is %d characters, over the 100 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("tagline must be exactly one line")
    return cleaned


def check_tagline_words(text):
    """Check the tagline says something specific about make.fun.

    A tagline that could sell anything is worth less than one that
    could only sell this site, so the line must name at least two of
    the three things make.fun is about: the agent, the bounty, and
    the reward. Returns the text or raises ValueError.
    """
    lowered = text.lower()
    hits = sum(word in lowered for word in ("agent", "bounty", "paid"))
    if hits < 2:
        raise ValueError(
            "tagline names only %d of agent/bounty/reward" % hits
        )
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_tagline(TAGLINE)
    text = check_tagline_words(text)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
