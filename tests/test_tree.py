import unittest
from src.models.node import Node
from src.models.tree import GeneralTree


class TestGeneralTree(unittest.TestCase):

    def setUp(self):
        self.tree = GeneralTree()
        self.root = Node("N1", "Rektor", "Rektor")
        self.tree.insert_node(None, self.root)

        self.child1 = Node("N2", "Dekan FST", "Dekan")
        self.child2 = Node("N3", "Dekan FT", "Dekan")
        self.tree.insert_node("N1", self.child1)
        self.tree.insert_node("N1", self.child2)

        self.subchild1 = Node("N4", "Kaprodi TIF", "Kaprodi")
        self.tree.insert_node("N2", self.subchild1)

    def test_insert_node_success(self):
        self.assertEqual(self.tree.get_total_nodes(), 4)
        self.assertEqual(self.tree.get_height(), 3)

    def test_insert_duplicate_id_fails(self):
        duplicate_node = Node("N1", "Duplikat", "Staff")
        with self.assertRaises(ValueError):
            self.tree.insert_node("N2", duplicate_node)

    def test_search_node_by_id(self):
        found = self.tree.search_node("N4", by="id")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].nama, "Kaprodi TIF")

    def test_search_node_by_nama(self):
        found = self.tree.search_node("Dekan", by="nama")
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0].id_pegawai, "N2")

    def test_search_node_by_jabatan(self):
        found = self.tree.search_node("Dekan", by="jabatan")
        self.assertEqual(len(found), 2)

    def test_search_non_existent(self):
        found = self.tree.search_node("GHOIB", by="id")
        self.assertEqual(len(found), 0)

    def test_preorder_traversal(self):
        result = [node.id_pegawai for node, _ in self.tree.preorder_traversal()]
        self.assertEqual(result, ["N1", "N2", "N4", "N3"])

    def test_inorder_traversal(self):
        result = [node.id_pegawai for node in self.tree.inorder_traversal()]
        self.assertEqual(result, ["N4", "N2", "N1", "N3"])

    def test_postorder_traversal(self):
        result = [node.id_pegawai for node in self.tree.postorder_traversal()]
        self.assertEqual(result, ["N4", "N2", "N3", "N1"])

    def test_levelorder_traversal(self):
        result = [node.id_pegawai for node, level in self.tree.levelorder_traversal()]
        self.assertEqual(result, ["N1", "N2", "N3", "N4"])


if __name__ == '__main__':
    unittest.main()
