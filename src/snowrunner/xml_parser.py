from __future__ import annotations

from pathlib import PurePosixPath
from xml.etree import ElementTree as ET

from .xml_document import XmlDocument


class XmlParser:
    """Parse SnowRunner XML files."""

    @staticmethod
    def parse(path: PurePosixPath, text: str) -> XmlDocument:
        """
        Parse a SnowRunner XML file.

        SnowRunner XML files frequently contain multiple top-level elements.
        Wrap the document in a temporary root element before parsing.
        """

        wrapped = f"<Document>\n{text}\n</Document>"

        root = ET.fromstring(wrapped)

        return XmlDocument(
            path=path,
            root=root,
        )
