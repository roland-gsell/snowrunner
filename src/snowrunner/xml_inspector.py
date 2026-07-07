from __future__ import annotations

from collections import defaultdict
from xml.etree.ElementTree import Element

from .xml_document import XmlDocument
from .xml_models import XmlNode, XmlTree


class XmlInspector:
    """Build a structural representation of an XML document."""

    @classmethod
    def inspect(cls, document: XmlDocument) -> XmlTree:
        """Inspect an XML document and return its structure."""

        return XmlTree(
            root=cls._inspect_element(document.root),
        )

    @classmethod
    def _inspect_element(
        cls,
        element: Element,
        occurrences: int = 1,
    ) -> XmlNode:
        """Recursively inspect an XML element."""

        grouped_children: dict[str, list[Element]] = defaultdict(list)

        for child in element:
            grouped_children[child.tag].append(child)

        children: list[XmlNode] = []

        for tag in sorted(grouped_children):
            elements = grouped_children[tag]

            children.append(
                cls._inspect_element(
                    elements[0],
                    occurrences=len(elements),
                )
            )

        return XmlNode(
            name=element.tag,
            occurrences=occurrences,
            attributes=tuple(sorted(element.attrib)),
            children=children,
        )
