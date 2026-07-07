from pathlib import PurePosixPath

from snowrunner.xml_parser import XmlParser


def test_parse_multiple_top_level_elements() -> None:
    text = """
<_templates Include="trucks"/>
<Truck Name="test_truck"/>
"""

    document = XmlParser.parse(
        PurePosixPath("test.xml"),
        text,
    )

    assert document.root.tag == "Document"

    children = [child.tag for child in document.root]

    assert children == ["_templates", "Truck"]
