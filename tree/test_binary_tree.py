from unittest import TestCase

from tree import binary_tree


class TestNode(TestCase):
    def test_binary_tree_single_node(self):
        root = binary_tree.Node(10)
        self.assertEqual(root.data, 10)

    def test_binary_tree_insert_node(self):
        root = binary_tree.Node(10)
        root.insert(20)
        root.insert(5)

        self.assertEqual(root.data, 10)
        self.assertEqual(root.left.data, 5)
        self.assertEqual(root.right.data, 20)