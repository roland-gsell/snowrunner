from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
from xml.etree.ElementTree import Element


@dataclass(frozen=True)
class XmlDocument:
    """Represents a parsed SnowRunner XML document."""

    path: PurePosixPath
    root: Element
