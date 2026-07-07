from pathlib import PurePosixPath

from snowrunner.xml_inspector import XmlInspector
from snowrunner.xml_parser import XmlParser


def test_group_repeated_elements() -> None:
    text = """
<A>
    <B foo="1"/>
    <B foo="2"/>
    <C/>
</A>
"""

    document = XmlParser.parse(
        PurePosixPath("test.xml"),
        text,
    )

    tree = XmlInspector.inspect(document)

    document_node = tree.root

    assert document_node.name == "Document"

    assert len(document_node.children) == 1

    a = document_node.children[0]

    assert a.name == "A"

    assert len(a.children) == 2

    assert a.children[0].name == "B"
    assert a.children[0].occurrences == 2
    assert a.children[0].attributes == ("foo",)

    assert a.children[1].name == "C"
    assert a.children[1].occurrences == 1
