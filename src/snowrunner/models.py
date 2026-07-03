#!/usr/bin/env python3

"""
SnowRunner Toolkit

Shared data models.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class DirectoryStatistics:
    """Statistics for a single archive directory."""

    path: PurePosixPath
    xml_files: int
    subdirectories: int
