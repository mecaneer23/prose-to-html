#!/usr/bin/env python3
"""Convert a file of prose into HTML paragraphs"""

from argparse import ArgumentParser, Namespace


def parse_args() -> Namespace:
    """Parse command line arguments"""
    parser = ArgumentParser()
    parser.add_argument("filename", nargs="?", default="file.txt")
    return parser.parse_args()


def main() -> None:
    """Entry point for Prose to HTML"""
    filename = parse_args().filename
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()

    contents = "<p>" + contents
    for old in ("\n", "\r", "\n\r"):
        contents = contents.replace(old, "</p>\n<p>")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(contents + "</p>")


if __name__ == "__main__":
    main()
