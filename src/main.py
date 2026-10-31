import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.organization_service import OrganizationService


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("=" * 75)
    print("      SISTEM MANAJEMEN SILSILAH ORGANISASI (GENERAL TREE ADT)      ")
    print("      UIN SULTAN SYARIF KASIM RIAU - FAKULTAS SAINS DAN TEKNOLOGI   ")
    print("=" * 75)


def handle_show_ascii_tree(service: OrganizationService):
    print("\n--- [1] HIERARKI SILSILAH ORGANISASI (ASCII TREE) ---")
    tree_str = service.generate_ascii_tree()
    print(tree_str)
    print("-" * 60)
    print(f"Total Pegawai: {service.tree.get_total_nodes()} | Tinggi Tree: {service.tree.get_height()}")


def handle_insert_employee(service: OrganizationService):
    print("\n--- [2] TAMBAH PEGAWAI BARU (OPERASI INSERT NODE) ---")
    parent_id = input("Masukkan ID Atasan Langsung (misal: PEG-004): ").strip()
    id_pegawai = input("Masukkan ID Pegawai Baru (misal: PEG-008)   : ").strip()
    nama = input("Masukkan Nama Lengkap Pegawai Baru          : ").strip()
    jabatan = input("Masukkan Jabatan Pegawai Baru               : ").strip()

    success, message = service.add_employee(id_pegawai, nama, jabatan, parent_id)
    if success:
        print(f"\n✅ SUCCESS: {message}")
    else:
        print(f"\n❌ ERROR: {message}")


def handle_search_employee(service: OrganizationService):
    print("\n--- [3] CARI PEGAWAI (OPERASI SEARCH NODE - DFS) ---")
    print("Pilih Kriteria Pencarian:")
    print("1. Berdasarkan ID Pegawai")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Jabatan")
    kriteria_choice = input("Pilihan (1-3): ").strip()

    by_map = {"1": "id", "2": "nama", "3": "jabatan"}
    by_type = by_map.get(kriteria_choice, "nama")

    keyword = input(f"Masukkan Kata Kunci {by_type.upper()}: ").strip()
    
    results_node = service.search_employee(keyword, search_type=by_type)

    if results_node:
        print(f"\n✅ DITEMUKAN {len(results_node)} DATA PEGAWAI:")
        for idx, result_node in enumerate(results_node, 1):
            print(f"\n[{idx}] Data Pegawai:")
            print(f"   - ID Pegawai : {result_node.id_pegawai}")
            print(f"   - Nama       : {result_node.nama}")
            print(f"   - Jabatan    : {result_node.jabatan}")
            
            atasan = result_node.parent.nama if result_node.parent else "N/A (Root/Rektor)"
            print(f"   - Atasan     : {atasan}")
            print(f"   - Jumlah Bawahan Langsung (Degree): {result_node.get_degree()}")
            
            if result_node.children:
                bawahan_str = ", ".join([child.nama for child in result_node.children])
                print(f"   - Daftar Bawahan: {bawahan_str}")
    else:
        print(f"\n❌ DATA TIDAK DITEMUKAN: Pegawai dengan {by_type} '{keyword}' tidak ada dalam hirarki.")


def handle_run_traversals(service: OrganizationService):
    print("\n--- [4] EKSEKUSI ALGORITMA TRAVERSAL TREE ---")
    summary = service.get_traversal_summary()

    print("\n📌 1. PREORDER TRAVERSAL (Root -> Children / Top-Down Order):")
    print("   Deskripsi: Menelusuri dari Atasan Utama lalu turun ke cabang bawahan dari kiri ke kanan.")
    print("   Urutan Traversal:")
    for idx, (node, depth) in enumerate(summary["preorder_with_depth"], 1):
        indent = "  " * depth
        print(f"   {idx:02d}. {indent}└─ {node}")

    print("\n📌 2. INORDER TRAVERSAL (Leftmost Child -> Root -> Other Children):")
    print("   Deskripsi: Kunjungi anak pertama (sub-tree paling kiri), lalu Parent/Root, lalu sisa anak lainnya.")
    print("   Urutan Traversal:")
    for idx, node in enumerate(summary["inorder"], 1):
        print(f"   {idx:02d}. {node}")

    print("\n📌 3. POSTORDER TRAVERSAL (Children -> Root / Bottom-Up Order):")
    print("   Deskripsi: Menelusuri seluruh Bawahan terlebih dahulu sebelum mengunjungi Atasan/Root.")
    print("   Urutan Traversal:")
    for idx, node in enumerate(summary["postorder"], 1):
        print(f"   {idx:02d}. {node}")

    print("\n📌 4. LEVEL-ORDER TRAVERSAL (Breadth-First Search / BFS):")
    print("   Deskripsi: Menelusuri hirarki per tingkat/level jabatan dari atas ke bawah.")
    print("   Urutan Traversal:")
    for idx, (node, level) in enumerate(summary["levelorder"], 1):
        print(f"   {idx:02d}. [Level {level}] {node}")


def handle_analysis_metrics(service: OrganizationService):
    print("\n--- [5] ANALISIS METRIK & KOMPLEKSITAS KOMPUTASI ---")
    tree = service.tree
    total_nodes = tree.get_total_nodes()
    height = tree.get_height()

    print(f"📊 Metrik Struktur Data Tree:")
    print(f"   • Total Simpul (N)      : {total_nodes} Node")
    print(f"   • Tinggi Pohon (Height) : {height} Level")
    print(f"   • Derajat Root (Rektor) : {tree.root.get_degree() if tree.root else 0} Sub-organisasi")
    
    print("\n🧠 Analisis Kompleksitas Algoritma (Struktur Data):")
    print("   1. Time Complexity Insert  : O(1) jika parent pointer diketahui; O(N) untuk pencarian DFS.")
    print("   2. Time Complexity Search  : Worst-Case O(N) DFS Rekursif (karena General Tree tidak terurut).")
    print("   3. Time Complexity Index   : O(1) Hash Table Lookup (_node_index untuk pencarian ID).")
    print("   4. Time Complexity Traversal: O(N) karena setiap simpul dikunjungi tepat satu kali.")
    print("   5. Space Complexity        : O(N) penyimpanan simpul dan stack rekursi DFS sebesar O(H).")

    print("\n📈 Pembahasan Bentuk Tree & Kecepatan Pencarian (Instruksi No. 4):")
    print("   a. Bentuk Pohon Organisasi:")
    print("      Pohon yang terbentuk bersifat TIDAK SEIMBANG (CONDONG / SKEWED) ke arah Fakultas Sains dan Teknologi (FST).")
    print("      - Cabang Wakil Rektor 1 tidak memiliki bawahan langsung (kedalaman hanya level 1).")
    print("      - Cabang FST condong memanjang ke bawah hingga level 3 (Dekan FST -> Kaprodi TIF -> Dosen/Staf).")
    print("   b. Seberapa Cepat Waktu Pencarian (Analisis Kompleksitas):")
    print("      - Berbeda dengan Binary Search Tree (BST) seimbang yang memiliki aturan partisi nilai kiri-kanan")
    print("        sehingga pencariannya bisa mencapai O(log N), General Tree adalah pohon tak-terurut.")
    print("      - Pada General Tree yang skewed, pencarian nama/jabatan tetap membutuhkan penelusuran menyeluruh (DFS).")
    print("      - Kompleksitas waktu pencarian terburuk (worst-case) adalah O(N), di mana N adalah jumlah total simpul.")
    print("      - Pada bentuk pohon yang skewed/condong ke dalam, overhead stack rekursi O(H) mendekati O(N).")
    print("      - Kesimpulan Optimasi: Untuk mengatasi kelemahan pohon skewed ini, sistem telah dilengkapi indeks")
    print("        HashMap internal sehingga pencarian berbasis ID tetap O(1) instan tanpa dipengaruhi bentuk pohon.")


def handle_soal_11(service: OrganizationService):
    print("\n" + "=" * 75)
    print("     [6] PENYELESAIAN SOAL NO. 11 (LEMBAR AKTIVITAS - IMAGE 2)")
    print("=" * 75)
    
    service.load_soal_11_sample_data()
    print("✅ Dataset Soal No. 11 Berhasil Dimuat ke dalam Tree!")
    
    print("\n🌳 Visualisasi Hierarki Pohon Soal No. 11:")
    print(service.generate_ascii_tree())

    summary = service.get_traversal_summary()
    pre_list = [node.jabatan for node in summary["preorder"]]
    in_list = [node.jabatan for node in summary["inorder"]]
    post_list = [node.jabatan for node in summary["postorder"]]

    print("\n📋 TABEL JAWABAN URUTAN TRAVERSAL SOAL NO. 11:")
    print("-" * 115)
    print(f"{'No':<4} | {'Pre-order (Root -> Anak)':<35} | {'In-order (Anak-1 -> Root -> Anak-N)':<35} | {'Post-order (Anak -> Root)':<35}")
    print("-" * 115)
    for i in range(len(pre_list)):
        print(f"{i+1:<4} | {pre_list[i]:<35} | {in_list[i]:<35} | {post_list[i]:<35}")
    print("-" * 115)


def main():
    service = OrganizationService()
    service.load_uin_suska_sample_data()

    while True:
        print_header()
        print(" [1] Tampilkan Hierarki Organisasi (ASCII Tree)")
        print(" [2] Sisipkan Pegawai Baru (insert_node)")
        print(" [3] Cari Data Pegawai (search_node - ID/Nama/Jabatan)")
        print(" [4] Jalankan Traversal (Preorder, Inorder, Postorder, Levelorder)")
        print(" [5] Tampilkan Metrik & Analisis Komputasi")
        print(" [6] image")
        print(" [0] Keluar")
        print("=" * 75)

        choice = input("Pilih Menu (0-6): ").strip()

        if choice == "1":
            handle_show_ascii_tree(service)
        elif choice == "2":
            handle_insert_employee(service)
        elif choice == "3":
            handle_search_employee(service)
        elif choice == "4":
            handle_run_traversals(service)
        elif choice == "5":
            handle_analysis_metrics(service)
        elif choice == "6":
            handle_soal_11(service)
        elif choice == "0":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\n❌ Pilihan tidak valid, silakan coba lagi.")

        input("\nTekan Enter untuk melanjutkan...")
        clear_screen()


if __name__ == "__main__":
    main()
