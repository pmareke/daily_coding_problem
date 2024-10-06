from typing import Self


class Node:
    def __init__(
        self,
        value: str,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.value = value
        self.left = left
        self.right = right


def serialize(node: Node) -> str:
    return node.value


def deserialize(data: str) -> Node:
    return Node(data)
