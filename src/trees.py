from typing import Self

"""
This problem was asked by Google.

Given the root to a binary tree:
    - Implement the `serialize(node)` function which serializes the node into a string.
    - Implement the `deserialize(string)` function which deserializes the string back into the Node.
"""


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
