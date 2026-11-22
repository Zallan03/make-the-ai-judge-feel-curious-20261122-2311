"""Write one short text to /output/entry.txt.

The text is a small, calm mystery: a lighthouse keeper, a light
that turns a half-second late, and a second cup of tea set out
for someone the light seems to be waiting for. Nothing is
explained; the reader is left wondering who it is waiting for.
"""

import os

TEXT = (
    "On the third night, the lighthouse keeper noticed the light "
    "turning a half-second late. He said nothing. He only put the "
    "kettle on, set out a second cup, and waited, in no hurry, to "
    "see who the light was waiting for."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
