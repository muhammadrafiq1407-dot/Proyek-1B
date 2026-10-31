from typing import List, Optional


class Node:
    def __init__(self, id_pegawai: str, nama: str, jabatan: str):
        if not id_pegawai or not id_pegawai.strip():
            raise ValueError("ID Pegawai tidak boleh kosong.")
        if not nama or not nama.strip():
            raise ValueError("Nama Pegawai tidak boleh kosong.")
        if not jabatan or not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong.")

        self._id_pegawai: str = id_pegawai.strip()
        self._nama: str = nama.strip()
        self._jabatan: str = jabatan.strip()
        self._parent: Optional['Node'] = None
        self._children: List['Node'] = []

    @property
    def id_pegawai(self) -> str:
        return self._id_pegawai

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def jabatan(self) -> str:
        return self._jabatan

    @property
    def parent(self) -> Optional['Node']:
        return self._parent

    @parent.setter
    def parent(self, parent_node: Optional['Node']) -> None:
        self._parent = parent_node

    @property
    def children(self) -> List['Node']:
        return list(self._children)

    def add_child(self, child_node: 'Node') -> None:
        if not isinstance(child_node, Node):
            raise TypeError("Objek child harus berupa instansiasi dari kelas Node.")
        if child_node is self:
            raise ValueError("Node tidak dapat menjadi child bagi dirinya sendiri.")
        
        child_node.parent = self
        self._children.append(child_node)

    def remove_child(self, child_node: 'Node') -> bool:
        if child_node in self._children:
            child_node.parent = None
            self._children.remove(child_node)
            return True
        return False

    def is_leaf(self) -> bool:
        return len(self._children) == 0

    def is_root(self) -> bool:
        return self._parent is None

    def get_degree(self) -> int:
        return len(self._children)

    def __repr__(self) -> str:
        return f"Node(ID='{self._id_pegawai}', Nama='{self._nama}', Jabatan='{self._jabatan}')"

    def __str__(self) -> str:
        return f"[{self._id_pegawai}] {self._nama} - {self._jabatan}"
