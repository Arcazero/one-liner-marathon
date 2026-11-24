"""One-Liner Marathon entry: write one original comedy joke to /output/entry.txt."""

import os

JOKE = "I taught my parrot to say 'per my last email' — now HR thinks the bird runs the department."


def main():
    # The gate requires UTF-8 text of 1-280 chars, not only whitespace,
    # on a single line. Guard it here so a bad joke can never ship.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} chars, must be 1-280"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE.strip(), "joke must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
