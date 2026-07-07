from pathlib import PurePosixPath

from snowrunner.pak_reader import PakReader
from snowrunner.xml_inspector import XmlInspector
from snowrunner.xml_parser import XmlParser


with PakReader("initial.pak") as reader:
    text = reader.read_text(
        PurePosixPath("[media]/classes/trucks/azov_5319.xml")
    )

document = XmlParser.parse(
    PurePosixPath("[media]/classes/trucks/azov_5319.xml"),
    text,
)

tree = XmlInspector.inspect(document)

print(tree)
