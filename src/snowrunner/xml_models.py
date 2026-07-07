from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class XmlNode:
    """Represents a node in an XML structure."""

    name: str
    occurrences: int = 1
    attributes: tuple[str, ...] = ()
    children: list["XmlNode"] = field(default_factory=list)


@dataclass(slots=True)
class XmlTree:
    """Represents the structure of an XML document."""

    root: XmlNode
