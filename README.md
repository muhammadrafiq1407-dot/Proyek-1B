# Proyek Silsilah Organisasi Berbasis General Tree ADT

Sistem manajemen hierarki silsilah organisasi kampus (Studi Kasus UIN Sultan Syarif Kasim Riau) yang dikembangkan menggunakan **Python berbasis Object-Oriented Programming (OOP) & Clean Architecture**.

## 📁 Struktur Direktori

```text
silsilah-organisasi/
├── .gitignore                     # Pengabaian berkas teracak Git
├── README.md                      # Petunjuk & dokumentasi proyek
├── requirements.txt               # Dependensi proyek
├── src/                           # Source code utama
│   ├── __init__.py
│   ├── main.py                    # Entry point aplikasi CLI
│   ├── models/                    # ADT & Layer Data
│   │   ├── __init__.py
│   │   ├── node.py                # Kelas Node (Atribut & Validation)
│   │   └── tree.py                # Kelas General Tree & Algoritma Traversal
│   └── services/                  # Business Logic Layer
│       ├── __init__.py
│       └── organization_service.py # Pengelola hirarki & formatter ASCII
└── tests/                         # Automated Unit Testing
    ├── __init__.py
    ├── test_node.py
    └── test_tree.py
```

## 🚀 Cara Menjalankan Aplikasi

1. **Jalankan Aplikasi Utama (CLI Menu):**
```bash
python3 src/main.py
```

2. **Jalankan Unit Test:**
```bash
python3 -m unittest discover -s tests
```
