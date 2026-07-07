from pathlib import PurePosixPath

from snowrunner.xml_parser import XmlParser


def test_parse_unbound_namespace_prefix() -> None:
    text = """
<Truck>
    <Dashboard>
        <region:default>
            <Gauge />
        </region:default>
    </Dashboard>
</Truck>
"""

    document = XmlParser.parse(
        PurePosixPath("test.xml"),
        text,
    )

    dashboard = document.root.find("./Truck/Dashboard")
    assert dashboard is not None

    region = dashboard.find("region_default")
    assert region is not None

    gauge = region.find("Gauge")
    assert gauge is not None
