from typing import List, Optional, Tuple, Dict
from src.models.node import Node
from src.models.tree import GeneralTree

Tuple_Bool_Str = Tuple[bool, str]


class OrganizationService:
    def __init__(self, tree: Optional[GeneralTree] = None):
        self._tree = tree if tree else GeneralTree()

    @property
    def tree(self) -> GeneralTree:
        return self._tree

    def load_uin_suska_sample_data(self) -> None:
        rektor = Node("PEG-001", "Prof. Dr. Khairunnas", "Rektor UIN Suska Riau")
        self._tree.set_root(rektor)

        wr1 = Node("PEG-002", "Dr. Helmiati, M.Ag", "Wakil Rektor 1 (Akademik)")
        dekan_fst = Node("PEG-003", "Prof. Dr. Okfalisa, ST, M.Sc", "Dekan Fakultas Sains dan Teknologi")
        
        self._tree.insert_node("PEG-001", wr1)
        self._tree.insert_node("PEG-001", dekan_fst)

        kaprodi_tif = Node("PEG-004", "Dr. Muhammad Said, M.T", "Ketua Prodi Teknik Informatika")
        kaprodi_si = Node("PEG-005", "Dr. Missi, M.Kom", "Ketua Prodi Sistem Informasi")

        self._tree.insert_node("PEG-003", kaprodi_tif)
        self._tree.insert_node("PEG-003", kaprodi_si)

        dosen_tif1 = Node("PEG-006", "Muhammad Rafiq Al-Ghifari", "Dosen/Asisten Pengajar TIF")
        dosen_tif2 = Node("PEG-007", "Staf Akademik TIF", "Staf Administrasi TIF")

        self._tree.insert_node("PEG-004", dosen_tif1)
        self._tree.insert_node("PEG-004", dosen_tif2)

    def load_soal_11_sample_data(self) -> None:
        self._tree = GeneralTree()

        rektor = Node("S11-01", "Rektor", "Rektor (Root)")
        self._tree.set_root(rektor)

        senat = Node("S11-02", "Senat Universitas", "Senat Universitas")
        wr1 = Node("S11-03", "Wakil Rektor I", "Wakil Rektor I (Bidang Akademik)")
        wr2 = Node("S11-04", "Wakil Rektor II", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)")
        wr3 = Node("S11-05", "Wakil Rektor III", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)")
        dekan = Node("S11-06", "Dekan FST", "Dekan Fakultas Sains dan Teknologi")

        self._tree.insert_node("S11-01", senat)
        self._tree.insert_node("S11-01", wr1)
        self._tree.insert_node("S11-01", wr2)
        self._tree.insert_node("S11-01", wr3)
        self._tree.insert_node("S11-01", dekan)

        wd1 = Node("S11-07", "Wakil Dekan I", "Wakil Dekan I (Bidang Akademik & Kelembagaan)")
        wd2 = Node("S11-08", "Wakil Dekan II", "Wakil Dekan II (Bidang AUPK)")
        wd3 = Node("S11-09", "Wakil Dekan III", "Wakil Dekan III (Bidang Kemahasiswaan)")
        kaprodi = Node("S11-10", "Kaprodi TIF", "Ketua Program Studi Teknik Informatika")

        self._tree.insert_node("S11-06", wd1)
        self._tree.insert_node("S11-06", wd2)
        self._tree.insert_node("S11-06", wd3)
        self._tree.insert_node("S11-06", kaprodi)

        sekprodi = Node("S11-11", "Sekretaris Prodi", "Sekretaris Program Studi")
        kalab = Node("S11-12", "Kepala Lab Komputer", "Kepala Laboratorium Komputer")
        koor_dosen = Node("S11-13", "Koordinator Dosen", "Koordinator Dosen")

        self._tree.insert_node("S11-10", sekprodi)
        self._tree.insert_node("S11-10", kalab)
        self._tree.insert_node("S11-10", koor_dosen)

        asisten = Node("S11-14", "Asisten Lab", "Asisten Laboratorium")
        teknisi = Node("S11-15", "Teknisi Lab", "Teknisi Laboratorium")

        self._tree.insert_node("S11-12", asisten)
        self._tree.insert_node("S11-12", teknisi)

        dpa = Node("S11-16", "DPA", "Dosen Pembimbing Akademik")
        dosen_mk = Node("S11-17", "Dosen Pengampu MK", "Dosen Pengampu Mata Kuliah")

        self._tree.insert_node("S11-13", dpa)
        self._tree.insert_node("S11-13", dosen_mk)

        mhs = Node("S11-18", "Mahasiswa Bimbingan", "Mahasiswa Bimbingan (Leaf)")
        self._tree.insert_node("S11-16", mhs)

    def add_employee(self, id_pegawai: str, nama: str, jabatan: str, parent_id: Optional[str]) -> Tuple_Bool_Str:
        try:
            new_node = Node(id_pegawai, nama, jabatan)
            self._tree.insert_node(parent_id, new_node)
            return True, f"Berhasil menambahkan '{nama}' ({jabatan}) ke dalam hirarki."
        except Exception as e:
            return False, str(e)

    def search_employee(self, keyword: str, search_type: str = "nama") -> List[Node]:
        return self._tree.search_node(key=keyword, by=search_type)

    def generate_ascii_tree(self, node: Optional[Node] = None, prefix: str = "", is_last: bool = True) -> str:
        if node is None:
            if self._tree.root is None:
                return "Pohon Hirarki Kosong."
            node = self._tree.root

        output = ""
        connector = "└── " if is_last else "├── "
        
        if node == self._tree.root:
            output += f"👑 {node}\n"
        else:
            output += f"{prefix}{connector}{node}\n"

        new_prefix = prefix + ("    " if is_last else "│   ")
        
        children = node.children
        for i, child in enumerate(children):
            is_child_last = (i == len(children) - 1)
            output += self.generate_ascii_tree(child, new_prefix, is_child_last)

        return output

    def get_traversal_summary(self) -> dict:
        preorder_raw = self._tree.preorder_traversal()
        inorder_raw = self._tree.inorder_traversal()
        postorder_raw = self._tree.postorder_traversal()
        levelorder_raw = self._tree.levelorder_traversal()

        return {
            "preorder": [node for node, _ in preorder_raw],
            "preorder_with_depth": preorder_raw,
            "inorder": inorder_raw,
            "postorder": postorder_raw,
            "levelorder": levelorder_raw
        }
