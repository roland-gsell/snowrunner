#!/usr/bin/env python3

"""
SnowRunner Toolkit

Archive exploration tool.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from archive_explorer import ArchiveExplorer
from pak_reader import PakReader


def print_statistics(explorer: ArchiveExplorer) -> None:
    """Print directory statistics."""

    statistics = explorer.directory_statistics("[media]/classes")

    print()
    print("Directory statistics")
    print("====================")
    print()

    print(f"{'Directory':45} {'XML':>5} {'DIRS':>5}")
    print("-" * 58)

    for stat in statistics:
        print(
            f"{stat.path.as_posix():45} "
            f"{stat.xml_files:>5} "
            f"{stat.subdirectories:>5}"
        )


def main() -> None:

    parser = argparse.ArgumentParser(
        description="SnowRunner archive explorer"
    )

    parser.add_argument(
        "pak",
        type=Path,
        help="Path to a SnowRunner PAK archive",
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show directory statistics",
    )

    args = parser.parse_args()

    with PakReader(args.pak) as reader:

        explorer = ArchiveExplorer(reader)

        if args.stats:
            print_statistics(explorer)
        else:
            print()
            print("Archive tree")
            print("============")
            print()

            explorer.tree("[media]", depth=2)


if __name__ == "__main__":
    main()
