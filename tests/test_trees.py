from expects import equal, expect

from src.trees import Node, deserialize, serialize

"""
This problem was asked by Google.

Given the root to a binary tree:
    - Implement the `serialize(node)` function which serializes the node into a string.
    - Implement the `deserialize(string)` function which deserializes the string back into the Node.
"""


class TestTrees:
    def test_serialize_single_node(self) -> None:
        root = Node("root")

        string_node = serialize(root)

        expect(string_node).to(equal('Node("root")'))

    def test_serialize_with_node_one_children(self) -> None:
        left = Node("left")
        root = Node("root", left)

        string_node = serialize(root)

        expect(string_node).to(equal('Node("root", Node("left"))'))

    def test_serialize_with_node_two_children(self) -> None:
        left = Node("left")
        right = Node("right")
        root = Node("root", left, right)

        string_node = serialize(root)

        expect(string_node).to(equal('Node("root", Node("left"), Node("right"))'))

    def test_deserialize_node(self) -> None:
        string_node = 'Node("root")'

        node = deserialize(string_node)

        expect(node.value).to(equal("root"))

    def test_deserialize_node_with_one_children(self) -> None:
        string_node = 'Node("root", Node("left"))'

        node = deserialize(string_node)

        assert node.left
        expect(node.left.value).to(equal("left"))

    def test_deserialize_node_with_two_children(self) -> None:
        string_node = 'Node("root", Node("left"), Node("right"))'

        node = deserialize(string_node)

        assert node.right
        expect(node.right.value).to(equal("right"))

    def test_solve(self) -> None:
        left_left = Node("left.left")
        left = Node("left", left_left)
        right = Node("right")
        root = Node("root", left, right)

        string_node = serialize(root)
        node = deserialize(string_node)

        assert node.left
        assert node.left.left
        expect(node.left.left.value).to(equal("left.left"))
