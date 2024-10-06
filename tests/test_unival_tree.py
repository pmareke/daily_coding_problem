from expects import equal, expect

from src.unival_tree import Node, count_unival_subtrees

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


class TestUnivalTree:
    def test_count_unival_subtrees(self) -> None:
        root = Node(
            "0",
            Node("1"),
            Node(
                "0",
                Node(
                    "1",
                    Node("1"),
                    Node("1"),
                ),
                Node("0"),
            ),
        )

        count = count_unival_subtrees(root)

        expect(count).to(equal(5))
