from pathlib import Path, PurePosixPath

from snowrunner.pak_reader import PakReader
from snowrunner.xml_parser import XmlParser


def main() -> None:
    pak_path = Path("initial.pak")

    with PakReader(pak_path) as reader:
        xml_text = reader.read_text(
            PurePosixPath("[media]/classes/trucks/azov_5319.xml")
        )

    document = XmlParser.parse(
        PurePosixPath("[media]/classes/trucks/azov_5319.xml"),
        xml_text,
    )

    print(f"Root: {document.root.tag}")
    print()

    print("Top-level elements:")
    for child in document.root:
        print(f"  {child.tag}")


if __name__ == "__main__":
    main()
