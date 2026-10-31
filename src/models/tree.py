from collections import deque
from typing import List, Optional, Tuple, Dict
from src.models.node import Node


class GeneralTree:
    def __init__(self, root_node: Optional[Node] = None):
        self._root: Optional[Node] = None
        self._node_index: Dict[str, Node] = {}
        
        if root_node:
            self.set_root(root_node)

    @property
    def root(self) -> Optional[Node]:
        return self._root

    def set_root(self, root_node: Node) -> None:
        if not isinstance(root_node, Node):
            raise TypeError("Root harus instansiasi dari kelas Node.")
        self._root = root_node
        self._node_index.clear()
        self._rebuild_index(self._root)

    def _rebuild_index(self, current_node: Optional[Node]) -> None:
        if current_node is None:
            return
        self._node_index[current_node.id_pegawai] = current_node
        for child in current_node.children:
            self._rebuild_index(child)

    def insert_node(self, parent_id: Optional[str], new_node: Node) -> bool:
        if not isinstance(new_node, Node):
            raise TypeError("Atribut new_node harus berupa objek kelas Node.")

        if new_node.id_pegawai in self._node_index:
            raise ValueError(f"Error: Node dengan ID '{new_node.id_pegawai}' sudah ada dalam sistem.")

        if self._root is None:
            self._root = new_node
            self._node_index[new_node.id_pegawai] = new_node
            return True

        if not parent_id:
            raise ValueError("parent_id wajib diisi karena Root sudah terdefinisi.")

        parent_nodes = self.search_node(key=parent_id, by="id")
        if not parent_nodes:
            raise KeyError(f"Error: Atasan dengan ID '{parent_id}' tidak ditemukan dalam struktur Tree.")

        parent_nodes = parent_nodes[0]
        parent_nodes.add_child(new_node)
        self._node_index[new_node.id_pegawai] = new_node
        return True

    def search_node(self, key: str, by: str = "nama", current_node: Optional[Node] = None) -> List[Node]:
        if self._root is None:
            return []

        if by == "id" and current_node is None:
            node = self._node_index.get(key)
            return [node] if node else []
        
        if current_node is None:
            current_node = self._root

        result_node: List[Node] = []

        target_val = getattr(current_node, 'id_pegawai' if by == "id" else ('nama' if by == "nama" else 'jabatan'))

        if by == "id":
            is_match = target_val.lower() == key.lower()
        else:
            is_match = key.lower() in target_val.lower()

        if is_match:
            result_node.append(current_node)

        for child in current_node.children:
            result_node.extend(self.search_node(key=key, by=by, current_node=child))

        return result_node

    def preorder_traversal(self, current_node: Optional[Node] = None, depth: int = 0) -> List[Tuple[Node, int]]:
        if current_node is None:
            if self._root is None:
                return []
            current_node = self._root

        result: List[Tuple[Node, int]] = [(current_node, depth)]

        for child in current_node.children:
            result.extend(self.preorder_traversal(current_node=child, depth=depth + 1))

        return result

    def inorder_traversal(self, current_node: Optional[Node] = None) -> List[Node]:
        if current_node is None:
            if self._root is None:
                return []
            current_node = self._root

        result: List[Node] = []
        children = current_node.children

        if len(children) > 0:
            result.extend(self.inorder_traversal(current_node=children[0]))

        result.append(current_node)

        for child in children[1:]:
            result.extend(self.inorder_traversal(current_node=child))

        return result

    def postorder_traversal(self, current_node: Optional[Node] = None) -> List[Node]:
        if current_node is None:
            if self._root is None:
                return []
            current_node = self._root

        result: List[Node] = []

        for child in current_node.children:
            result.extend(self.postorder_traversal(current_node=child))

        result.append(current_node)

        return result

    def levelorder_traversal(self) -> List[Tuple[Node, int]]:
        if self._root is None:
            return []

        result: List[Tuple[Node, int]] = []
        queue: deque[Tuple[Node, int]] = deque([(self._root, 0)])

        while queue:
            node, level = queue.popleft()
            result.append((node, level))
            for child in node.children:
                queue.append((child, level + 1))

        return result

    def get_height(self, current_node: Optional[Node] = None) -> int:
        if current_node is None:
            if self._root is None:
                return 0
            current_node = self._root

        if current_node.is_leaf():
            return 1

        return 1 + max(self.get_height(child) for child in current_node.children)

    def get_total_nodes(self) -> int:
        return len(self._node_index) if self._root else 0

    def get_ancestors(self, node_id: str) -> List[Node]:
        found_nodes = self.search_node(key=node_id, by="id")
        if not found_nodes:
            return []

        target_node = found_nodes[0]
        ancestors = []
        curr = target_node.parent
        while curr:
            ancestors.append(curr)
            curr = curr.parent
        return ancestors
