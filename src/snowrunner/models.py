from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class DirectoryStatistics:
    """Statistics for a single archive directory."""

    path: PurePosixPath
    xml_files: int
    subdirectories: int
