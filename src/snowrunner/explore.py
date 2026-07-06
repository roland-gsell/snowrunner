#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath

from archive_explorer import ArchiveExplorer
from pak_reader import PakReader


def cmd_tree(explorer: ArchiveExplorer, path: PurePosixPath) -> None:
    print()
    print("Archive tree")
    print("============")
    print()

    explorer.tree(path, depth=2)


def cmd_stats(explorer: ArchiveExplorer, path: PurePosixPath) -> None:
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


def cmd_ls(explorer: ArchiveExplorer, path: PurePosixPath) -> None:
    directories, files = explorer.list(path)

    print()
    print(path.as_posix())
    print("=" * len(path.as_posix()))
    print()

    if directories:
        print("Directories")
        print("-----------")
        for directory in directories:
            print(directory.name)
        print()

    if files:
        print("Files")
        print("-----")
        for file in files:
            print(file.name)
        print()


def cmd_find(explorer: ArchiveExplorer, query: str) -> None:
    query = query.lower()

    matches = [
        path
        for path in explorer.all_paths()
        if query in path.as_posix().lower()
    ]

    print()
    print(f"Search results for '{query}'")
    print("=" * (21 + len(query)))
    print()

    if not matches:
        print("No matches found.")
        return

    for match in matches:
        print(match.as_posix())


def cmd_cat(reader: PakReader, path: PurePosixPath) -> None:
    print(reader.read_text(path))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SnowRunner archive explorer"
    )

    parser.add_argument(
        "pak",
        type=Path,
        help="SnowRunner .pak archive",
    )

    parser.add_argument(
        "command",
        choices=[
            "tree",
            "stats",
            "ls",
            "find",
            "cat",
        ],
    )

    parser.add_argument(
        "argument",
        nargs="?",
        default="[media]",
        help="Archive path or search query",
    )

    args = parser.parse_args()

    with PakReader(args.pak) as reader:
        explorer = ArchiveExplorer(reader)

        if args.command == "tree":
            cmd_tree(explorer, PurePosixPath(args.argument))

        elif args.command == "stats":
            cmd_stats(explorer, PurePosixPath(args.argument))

        elif args.command == "ls":
            cmd_ls(explorer, PurePosixPath(args.argument))

        elif args.command == "find":
            cmd_find(explorer, args.argument)

        elif args.command == "cat":
            cmd_cat(reader, PurePosixPath(args.argument))


if __name__ == "__main__":
    main()
