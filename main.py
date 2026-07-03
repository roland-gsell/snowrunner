#!/usr/bin/env python3

"""
SnowRunner Database Project

Archive discovery tool.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pak_reader import PakReader


def print_section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


def main() -> None:

    parser = argparse.ArgumentParser(
        description="SnowRunner archive discovery tool."
    )

    parser.add_argument(
        "pak",
        type=Path,
        help="Path to a SnowRunner .pak file",
    )

    args = parser.parse_args()

    with PakReader(args.pak) as pak:

        print(f"Archive : {args.pak}")
        print(f"Files   : {pak.file_count()}")

        xml_files = pak.find_suffix(".xml")

        print(f"XML     : {len(xml_files)}")

        print_section("Top level directories")

        top = sorted(
            {
                path.parts[0]
                for path in pak.directories()
                if len(path.parts) > 0
            }
        )

        for directory in top:
            print(f"  {directory}")

        print_section("Truck directories")

        truck_dirs = sorted(
            {
                path.parent
                for path in pak.find_directory("[media]/classes/trucks")
                if "_tuning" not in str(path)
            }
        )

        for directory in truck_dirs:
            print(f"  {directory}")

        print_section("First 20 truck XML files")

        truck_files = [
            path
            for path in pak.find_directory("[media]/classes/trucks")
            if "_tuning" not in str(path)
            and path.suffix == ".xml"
        ]

        for path in truck_files[:20]:
            print(f"  {path.name}")


if __name__ == "__main__":
    main()
