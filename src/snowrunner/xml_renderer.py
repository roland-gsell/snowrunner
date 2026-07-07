from __future__ import annotations

from .xml_models import XmlNode, XmlTree


class XmlTreeRenderer:
    """Render an XmlTree as a human-readable tree."""

    @classmethod
    def render(cls, tree: XmlTree) -> str:
        """Render an XmlTree."""

        lines: list[str] = []

        cls._render_node(
            node=tree.root,
            lines=lines,
            prefix="",
            is_last=True,
        )

        return "\n".join(lines)

    @classmethod
    def _render_node(
        cls,
        node: XmlNode,
        lines: list[str],
        prefix: str,
        is_last: bool,
    ) -> None:
        """Render a single XmlNode recursively."""

        connector = "└── " if is_last else "├── "

        if prefix:
            line = prefix + connector
        else:
            line = ""

        line += node.name

        if node.occurrences > 1:
            line += f" (x{node.occurrences})"

        if node.attributes:
            line += " [" + ", ".join(node.attributes) + "]"

        lines.append(line)

        child_prefix = prefix + ("    " if is_last else "│   ")

        for index, child in enumerate(node.children):
            cls._render_node(
                node=child,
                lines=lines,
                prefix=child_prefix,
                is_last=index == len(node.children) - 1,
            )
