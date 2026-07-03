#!/usr/bin/env python3

"""
SnowRunner Database Project

Archive exploration tool.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from archive_explorer import ArchiveExplorer
from pak_reader import PakReader


def main() -> None:

    parser = argparse.ArgumentParser(
        description="SnowRunner archive explorer"
    )

    parser.add_argument(
        "pak",
        type=Path,
        help="Path to a SnowRunner PAK archive",
    )

    args = parser.parse_args()

    with PakReader(args.pak) as reader:

        explorer = ArchiveExplorer(reader)

        print()
        print("Archive tree")
        print("============")
        print()

        explorer.tree("[media]", depth=2)


if __name__ == "__main__":
    main()
