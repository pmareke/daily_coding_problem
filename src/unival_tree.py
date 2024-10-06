from dataclasses import dataclass
from typing import Self

"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


@dataclass
class Node:
    value: str
    left: Self | None = None
    right: Self | None = None


def count_unival_subtrees(node: Node) -> int:
    _, count = _is_unival(node)
    return count


def _is_unival(node: Node | None, count: int = 0) -> tuple[bool, int]:
    if not node:
        return (True, count)

    left_is_unival, count = _is_unival(node.left, count)
    right_is_unival, count = _is_unival(node.right, count)

    if left_is_unival and right_is_unival:
        if node.left and node.left.value != node.value:
            return (False, count)
        if node.right and node.right.value != node.value:
            return (False, count)
        count += 1
        return (True, count)

    return (False, count)
