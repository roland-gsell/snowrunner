from __future__ import annotations

from collections import defaultdict
from pathlib import PurePosixPath

from models import DirectoryStatistics
from pak_reader import PakReader


class ArchiveExplorer:
    """Provide filesystem-like navigation inside a PAK archive."""

    def __init__(self, reader: PakReader):
        self._reader = reader

        self._directories: dict[
            PurePosixPath,
            tuple[list[PurePosixPath], list[PurePosixPath]],
        ] = {}

        self._build_index()

    def _build_index(self) -> None:
        directory_map: dict[
            PurePosixPath,
            dict[str, set | list],
        ] = defaultdict(lambda: {"directories": set(), "files": []})

        for path in self._reader.list_files():
            parent = path.parent
            directory_map[parent]["files"].append(path)

            current = parent
            while current != current.parent:
                directory_map[current.parent]["directories"].add(current)
                current = current.parent

        self._directories = {
            directory: (
                sorted(content["directories"]),
                sorted(content["files"]),
            )
            for directory, content in directory_map.items()
        }

    # -------------------------
    # FIXED: safe + deduplicated
    # -------------------------
    def all_paths(self) -> list[PurePosixPath]:
        """Return all unique file paths in the archive."""

        seen: set[PurePosixPath] = set()

        for _, (_, files) in self._directories.items():
            for f in files:
                seen.add(f)

        return sorted(seen, key=lambda p: p.as_posix())

    def list(
        self,
        directory: str | PurePosixPath,
    ) -> tuple[list[PurePosixPath], list[PurePosixPath]]:
        directory = PurePosixPath(directory)
        return self._directories.get(directory, ([], []))

    def directory_statistics(
        self,
        directory: str | PurePosixPath,
    ) -> list[DirectoryStatistics]:
        directory = PurePosixPath(directory)

        directories, _ = self.list(directory)

        stats: list[DirectoryStatistics] = []

        for subdir in directories:
            child_dirs, child_files = self.list(subdir)

            xml_count = sum(
                1 for f in child_files if f.suffix.lower() == ".xml"
            )

            stats.append(
                DirectoryStatistics(
                    path=subdir,
                    xml_files=xml_count,
                    subdirectories=len(child_dirs),
                )
            )

        return sorted(stats, key=lambda s: s.path.as_posix())

    def tree(self, directory: str | PurePosixPath, depth: int = 2) -> None:
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
