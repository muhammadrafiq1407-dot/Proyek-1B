import unittest
from src.models.node import Node


class TestNode(unittest.TestCase):

    def test_node_creation_valid(self):
        node = Node("P01", "Rafiq", "Rektor")
        self.assertEqual(node.id_pegawai, "P01")
        self.assertEqual(node.nama, "Rafiq")
        self.assertEqual(node.jabatan, "Rektor")
        self.assertIsNone(node.parent)
        self.assertEqual(len(node.children), 0)

    def test_node_creation_invalid(self):
        with self.assertRaises(ValueError):
            Node("", "Rafiq", "Rektor")
        with self.assertRaises(ValueError):
            Node("P01", "   ", "Rektor")

    def test_add_child_relationship(self):
        parent = Node("P01", "Rektor", "Rektor")
        child = Node("P02", "Dekan", "Dekan")

        parent.add_child(child)

        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0], child)
        self.assertEqual(child.parent, parent)
        self.assertFalse(parent.is_leaf())
        self.assertTrue(child.is_leaf())

    def test_add_self_as_child_fails(self):
        node = Node("P01", "Rektor", "Rektor")
        with self.assertRaises(ValueError):
            node.add_child(node)


if __name__ == '__main__':
    unittest.main()
