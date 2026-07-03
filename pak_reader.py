#!/usr/bin/env python3

"""
SnowRunner Database Project

PAK reader implementation.

SnowRunner .pak files are ZIP archives containing XML resources,
textures, sounds and other game assets.
"""

from __future__ import annotations

from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile


class PakReader:
    """Read files from a SnowRunner PAK archive."""

    def __init__(self, pak_path: Path | str):

        self.path = Path(pak_path)

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        try:
            self._zip = ZipFile(self.path, "r")
        except BadZipFile as exc:
            raise RuntimeError(
                f"{self.path} is not a valid ZIP/PAK archive."
            ) from exc

        self._files = tuple(
            PurePosixPath(name.replace("\\", "/"))
            for name in self._zip.namelist()
        )

        self._file_set = frozenset(self._files)

    def close(self) -> None:
        self._zip.close()

    def file_count(self) -> int:
        return len(self._files)

    def list_files(self) -> list[PurePosixPath]:
        return list(self._files)

    def exists(self, filename: str | PurePosixPath) -> bool:
        return PurePosixPath(filename) in self._file_set

    def read_bytes(self, filename: str | PurePosixPath) -> bytes:
        archive_name = str(PurePosixPath(filename)).replace("/", "\\")
        return self._zip.read(archive_name)

    def read_text(
        self,
        filename: str | PurePosixPath,
        encoding: str = "utf-8",
    ) -> str:
        return self.read_bytes(filename).decode(encoding)

    def find_suffix(self, suffix: str) -> list[PurePosixPath]:
        suffix = suffix.lower()

        return sorted(
            path
            for path in self._files
            if path.name.lower().endswith(suffix)
        )

    def find_directory(self, directory: str) -> list[PurePosixPath]:

        directory = directory.replace("\\", "/").rstrip("/")

        return sorted(
            path
            for path in self._files
            if str(path.parent).startswith(directory)
        )

    def directories(self) -> list[PurePosixPath]:

        dirs: set[PurePosixPath] = set()

        for path in self._files:
            parent = path.parent

            while str(parent) not in ("", "."):
                dirs.add(parent)
                parent = parent.parent

        return sorted(dirs)

    def __enter__(self) -> "PakReader":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()
