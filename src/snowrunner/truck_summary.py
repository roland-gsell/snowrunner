from __future__ import annotations

from .xml_document import XmlDocument


SECTIONS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    (
        "General",
        "./Truck/TruckData",
        (
            "TruckType",
            "FuelCapacity",
            "DiffLockType",
        ),
    ),
    (
        "Engine",
        "./Truck/TruckData/EngineSocket",
        (
            "Default",
            "Type",
        ),
    ),
    (
        "Gearbox",
        "./Truck/TruckData/GearboxSocket",
        (
            "Default",
            "Type",
        ),
    ),
    (
        "Suspension",
        "./Truck/TruckData/SuspensionSocket",
        (
            "Default",
            "Type",
        ),
    ),
    (
        "Wheels",
        "./Truck/TruckData/Wheels",
        (
            "DefaultWheelType",
            "DefaultTire",
            "DefaultRim",
        ),
    ),
)


def render(document: XmlDocument) -> str:
    """Render a concise truck summary."""

    lines: list[str] = []

    lines.append("Truck Summary")
    lines.append("=============")

    for title, xpath, attributes in SECTIONS:
        element = document.root.find(xpath)

        if element is None:
            continue

        lines.append("")
        lines.append(title)
        lines.append("-" * len(title))

        for attribute in attributes:
            value = element.get(attribute)

            if value is None:
                continue

            lines.append(f"{attribute:20} {value}")

    return "\n".join(lines)
