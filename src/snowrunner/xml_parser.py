from __future__ import annotations

import re

from pathlib import PurePosixPath
from xml.etree import ElementTree as ET

from .xml_document import XmlDocument


class XmlParser:
    """Parse SnowRunner XML files."""

    @staticmethod
    def _normalize(text: str) -> str:
        """Normalize SnowRunner-specific XML syntax."""
    
        # Replace namespace-like prefixes with underscores.
        #
        # Example:
        #     <region:default> -> <region_default>
        #     </region:default> -> </region_default>
        #
        # SnowRunner uses namespace-like prefixes without declaring XML
        # namespaces, which standard XML parsers reject.
    
        return re.sub(
            r"(<\/?)([A-Za-z_][\w.-]*):([A-Za-z_][\w.-]*)",
            r"\1\2_\3",
            text,
        )

    @staticmethod
    def parse(path: PurePosixPath, text: str) -> XmlDocument:
        """
        Parse a SnowRunner XML file.

        SnowRunner XML files frequently contain multiple top-level elements.
        Wrap the document in a temporary root element before parsing.
        """

        normalized = XmlParser._normalize(text)

        wrapped = f"<Document>\n{normalized}\n</Document>"

        root = ET.fromstring(wrapped)

        return XmlDocument(
            path=path,
            root=root,
        )
