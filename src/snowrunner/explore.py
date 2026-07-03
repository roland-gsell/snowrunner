#!/usr/bin/env python3

"""
SnowRunner Toolkit

Archive exploration CLI.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from archive_explorer import ArchiveExplorer
from pak_reader import PakReader


# -----------------------------
# Command implementations
# -----------------------------

def cmd_tree(explorer: ArchiveExplorer, path: str) -> None:
    print()
    print("Archive tree")
    print("============")
    print()

    explorer.tree(path, depth=2)


def cmd_stats(explorer: ArchiveExplorer, path: str) -> None:
    statistics = explorer.directory_statistics(path)

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


def cmd_ls(explorer: ArchiveExplorer, path: str) -> None:
    directories, files = explorer.list(path)

    print()
    print(path)
    print("=" * len(path))
    print()

    if directories:
        print("Directories")
        print("-----------")
        for d in directories:
            print(d.name)
        print()

    if files:
        print("Files")
        print("-----")
        for f in files:
            print(f.name)
        print()


# -----------------------------
# CLI entry point
# -----------------------------

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
        "command",
        choices=["tree", "stats", "ls"],
        help="Command to execute",
    )

    parser.add_argument(
        "path",
        nargs="?",
        default="[media]",
        help="Archive path (default: [media])",
    )

    args = parser.parse_args()

    with PakReader(args.pak) as reader:
        explorer = ArchiveExplorer(reader)

        if args.command == "tree":
            cmd_tree(explorer, args.path)

        elif args.command == "stats":
            cmd_stats(explorer, args.path)

        elif args.command == "ls":
            cmd_ls(explorer, args.path)


if __name__ == "__main__":
    main()
