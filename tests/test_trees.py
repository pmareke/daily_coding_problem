from expects import equal, expect

from src.trees import Node, deserialize, serialize

"""
This problem was asked by Google.

Given the root to a binary tree:
    - Implement the `serialize(node)` function which serializes the node into a string.
    - Implement the `deserialize(string)` function which deserializes the string back into the Node.
"""


class TestTrees:
    def test_serialize_tree(self) -> None:
        pass

    def test_deserialize_tree(self) -> None:
        pass

    def test_solve(self) -> None:
        left_left = Node("left.left")
        left = Node("left", left_left)
        right = Node("right")
        root = Node("root", left, right)

        string_node = serialize(root)
        node = deserialize(string_node)

        expect(node.left.left.value).to(equal("left.left"))
