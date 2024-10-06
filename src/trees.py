from dataclasses import dataclass
from typing import Self

"""
This problem was asked by Google.

Given the root to a binary tree:
    - Implement the `serialize(node)` function which serializes the node into a string.
    - Implement the `deserialize(string)` function which deserializes the string back into the Node.
"""


@dataclass
class Node:
    value: str
    left: Self | None = None
    right: Self | None = None


def serialize(node: Node) -> str:
    if not node.left and not node.right:
        return f'Node("{node.value}")'
    if not node.left:
        assert node.right
        return f'Node("{node.value}", {serialize(node.right)})'
    if not node.right:
        assert node.left
        return f'Node("{node.value}", {serialize(node.left)})'
    return f'Node("{node.value}", {serialize(node.left)}, {serialize(node.right)})'


def deserialize(data: str) -> Node:
    node: Node = eval(data)
    return node
