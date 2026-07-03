from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Iterable


ENGINE_RE = re.compile(r"<Engine>(.*?)</Engine>", re.IGNORECASE)
GEARBOX_RE = re.compile(r"<Gearbox>(.*?)</Gearbox>", re.IGNORECASE)


@dataclass(frozen=True)
class TruckDependencies:
    truck_file: PurePosixPath
    engines: list[str]
    gearboxes: list[str]


class TruckDependencyExtractor:
    """
    Extracts simple dependency relations from truck XML files.

    This is intentionally minimal:
    - no schema assumptions
    - no game logic interpretation
    """

    def __init__(self, xml_files: dict[PurePosixPath, str]):
        """
        xml_files: mapping of path -> file content
        """
        self._xml_files = xml_files

    def extract_all(self) -> list[TruckDependencies]:
        results: list[TruckDependencies] = []

        for path, content in self._xml_files.items():

            if "/trucks/" not in path.as_posix():
                continue

            engines = ENGINE_RE.findall(content)
            gearboxes = GEARBOX_RE.findall(content)

            results.append(
                TruckDependencies(
                    truck_file=path,
                    engines=engines,
                    gearboxes=gearboxes,
                )
            )

        return results
