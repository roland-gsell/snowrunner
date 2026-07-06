from __future__ import annotations

import zipfile
from pathlib import Path, PurePosixPath


class PakReader:
    """Minimal SnowRunner PAK archive reader."""

    def __init__(self, path: Path):
        self._path = path
        self._zip: zipfile.ZipFile | None = None
        self._archive_map: dict[PurePosixPath, str] = {}

    def __enter__(self) -> "PakReader":
        self._zip = zipfile.ZipFile(self._path, "r")

        self._archive_map = {}

        for name in self._zip.namelist():
            if name.endswith("/"):
                continue

            normalized = PurePosixPath(name.replace("\\", "/"))
            self._archive_map[normalized] = name

        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._zip is not None:
            self._zip.close()

    def list_files(self) -> list[PurePosixPath]:
        """Return all files inside the archive."""

        return sorted(self._archive_map.keys())

    def read_text(self, path: PurePosixPath) -> str:
        """Read a text file from the archive."""

        assert self._zip is not None

        archive_name = self._archive_map[path]

        with self._zip.open(archive_name) as fp:
            return fp.read().decode("utf-8", errors="replace")
