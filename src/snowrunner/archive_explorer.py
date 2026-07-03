#!/usr/bin/env python3

"""
SnowRunner Toolkit

Archive explorer for SnowRunner PAK files.
"""

from __future__ import annotations

from pathlib import PurePosixPath

from models import DirectoryStatistics
from pak_reader import PakReader


class ArchiveExplorer:
    """Provide filesystem-like navigation inside a PAK archive."""

    def __init__(self, reader: PakReader):
        self._reader = reader

    def list(
        self,
        directory: str | PurePosixPath,
    ) -> tuple[list[PurePosixPath], list[PurePosixPath]]:
        """
        Return the immediate subdirectories and files of a directory.
        """

        directory = PurePosixPath(directory)

        directories: set[PurePosixPath] = set()
        files: list[PurePosixPath] = []

        for path in self._reader.list_files():

            try:
                relative = path.relative_to(directory)
            except ValueError:
                continue

            if len(relative.parts) == 1:
                files.append(path)

            elif len(relative.parts) > 1:
                directories.add(directory / relative.parts[0])

        return sorted(directories), sorted(files)

    def directory_statistics(
        self,
        directory: str | PurePosixPath,
    ) -> list[DirectoryStatistics]:
        """
        Return statistics for the immediate child directories.
        """

        directory = PurePosixPath(directory)

        directories, _ = self.list(directory)

        statistics: list[DirectoryStatistics] = []

        for subdir in directories:

            child_dirs, child_files = self.list(subdir)

            xml_count = sum(
                1
                for file in child_files
                if file.suffix.lower() == ".xml"
            )

            statistics.append(
                DirectoryStatistics(
                    path=subdir,
                    xml_files=xml_count,
                    subdirectories=len(child_dirs),
                )
            )

        return sorted(statistics, key=lambda stat: stat.path.as_posix())

    def tree(self, directory: str | PurePosixPath, depth: int = 2) -> None:
        """Print a directory tree."""

        directory = PurePosixPath(directory)

        self._print(directory, depth, 0)

    def _print(
        self,
        directory: PurePosixPath,
        depth: int,
        level: int,
    ) -> None:

        indent = "    " * level

        print(f"{indent}{directory.name or directory}")

        if depth == 0:
            return

        directories, files = self.list(directory)

        for subdir in directories:
            self._print(subdir, depth - 1, level + 1)

        for file in files:
            print(f"{indent}    {file.name}")
