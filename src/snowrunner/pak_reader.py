from __future__ import annotations

import zipfile
from pathlib import Path, PurePosixPath


class PakReader:
    """
    Minimal SnowRunner PAK archive reader.

    Wraps a zipfile and exposes normalized POSIX paths.
    """

    def __init__(self, path: Path):
        self._path = path
        self._zip: zipfile.ZipFile | None = None

    def __enter__(self) -> "PakReader":
        self._zip = zipfile.ZipFile(self._path, "r")
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        if self._zip:
            self._zip.close()

    # -----------------------------
    # Existing API
    # -----------------------------

    def list_files(self) -> list[PurePosixPath]:
        assert self._zip is not None

        return [
            PurePosixPath(name)
            for name in self._zip.namelist()
            if not name.endswith("/")
        ]

    # -----------------------------
    # NEW: file content access
    # -----------------------------

    def read_file(self, path: PurePosixPath | str) -> str:
        """
        Read a file from the archive as text.

        Assumes XML/text content (UTF-8 safe fallback).
        """
        assert self._zip is not None

        path_str = str(path)

        with self._zip.open(path_str) as f:
            return f.read().decode("utf-8", errors="replace")
