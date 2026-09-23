<div align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="80" height="80" alt="Python">

# Python Learning

Belajar Python dari nol sampai lanjutan dengan pendekatan bertahap dan berbasis proyek.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

</div>

## Identitas

| | |
|---|---|
| **Nama** | Syauqi Nuzul Abdi |
| **NIM** | 202512042 |
| **Mata Kuliah** | Pemrograman Berorientasi Objek |

---

## Tujuan

Membangun pemahaman Python secara bertahap: dari variabel dan tipe data, OOP, file handling, NumPy/Pandas/Matplotlib, machine learning dasar, database, hingga Django. Semuanya digabungkan dalam satu final project.

Kurikulum mengikuti urutan materi [W3Schools Python Tutorial](https://www.w3schools.com/python/) sebagai acuan struktur belajar. Seluruh penjelasan, contoh kode, dan mini project ditulis ulang secara original.

## Roadmap Belajar

| No | Topik | Folder | Isi |
|----|-------|--------|-----|
| 1 | Fundamentals | `01_fundamentals/` | Sintaks dasar sampai operator |
| 2 | Data Structures | `02_data_structures/` | List, tuple, set, dictionary |
| 3 | Control Flow | `03_control_flow/` | if/else, match, perulangan |
| 4 | Functions | `04_functions/` | Function, lambda, scope, module |
| 5 | Advanced Basics | `05_advanced_basics/` | datetime, json, regex, try/except, venv |
| 6 | OOP | `06_oop/` | Class, inheritance, polymorphism, encapsulation |
| 7 | File Handling | `07_file_handling/` | Membaca, menulis, dan menghapus file |
| 8 | Libraries | `07_libraries/` | NumPy, Pandas, SciPy, Matplotlib |
| 9 | Machine Learning | `08_machine_learning/` | Statistik dasar sampai KNN |
| 10 | Database | `09_database/` | MySQL dan MongoDB |
| 11 | Django | `10_django/` | Pengenalan web framework |
| 12 | Mini Projects | `mini_projects/` | 15 proyek kecil bertahap |
| 13 | Final Project | `projects/final_project/` | Student Management System |

Checklist progres per topik ada di [PROGRESS.md](PROGRESS.md).

## Struktur Folder

```
learn-python/
├── README.md
├── PROGRESS.md
├── requirements.txt
├── .gitignore
├── .env.example
├── 01_fundamentals/
├── 02_data_structures/
├── 03_control_flow/
├── 04_functions/
├── 05_advanced_basics/
├── 06_oop/
├── 07_file_handling/
├── 07_libraries/
│   ├── numpy/
│   ├── pandas/
│   ├── scipy/
│   └── matplotlib/
├── 08_machine_learning/
├── 09_database/
│   ├── mysql/
│   └── mongodb/
├── 10_django/
├── exercises/
│   ├── beginner/
│   ├── intermediate/
│   └── advanced/
├── solutions/
├── mini_projects/
│   └── 01_calculator/ ... 15_expense_analyzer/
└── projects/
    └── final_project/
```

## Instalasi

**Prasyarat**

- Python 3.10 atau lebih baru (dibutuhkan untuk fitur `match`)
- Visual Studio Code
- Koneksi internet untuk `pip install`

**Langkah-langkah**

```bash
# 1. Clone repository
git clone https://github.com/Jouqio/learn-python.git
cd learn-python

# 2. Buat virtual environment
python -m venv .venv

# 3. Aktifkan virtual environment
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

# 4. Install dependencies
pip install -r requirements.txt
```

Untuk menonaktifkan virtual environment, jalankan `deactivate`.

**Pengaturan VS Code**

1. Buka folder `learn-python` di VS Code.
2. Install ekstensi **Python** (Microsoft) dan **Pylance**.
3. Pilih interpreter `.venv` lewat `Ctrl+Shift+P` → `Python: Select Interpreter`.

## Cara Menjalankan

Setiap file materi bisa langsung dijalankan:

```bash
python 01_fundamentals/01_home.py
```

Mini project dan final project punya `main.py` masing-masing:

```bash
python mini_projects/01_calculator/main.py
python projects/final_project/main.py
```

## Format File Materi

Setiap file topik (`01_....py` sampai `94_....py`) ditulis singkat dan mudah dipahami pemula, dengan tiga bagian:

1. **KONSEP** | penjelasan singkat topik.
2. **CONTOH** | kode sederhana yang bisa langsung dijalankan.
3. **RANGKUMAN** | poin penting yang perlu diingat.

Latihan tambahan tersedia di folder `exercises/`, dengan jawaban referensi di `solutions/`.

## Konfigurasi Database

Kredensial database **tidak boleh** ditulis langsung di kode. Salin `.env.example` menjadi `.env`, lalu isi nilainya sesuai lingkungan Anda.

```bash
cp .env.example .env
```

## Mini Projects dan Final Project

- **Mini Projects** | 15 proyek bertahap di `mini_projects/`, dari kalkulator sederhana sampai analisis data dengan pandas. Tiap proyek punya `README.md`, `main.py`, dan `requirements.txt`.
- **Final Project** | *Student Management System* di `projects/final_project/`, sebuah aplikasi CLI lengkap yang menggabungkan variables, data types, conditions, loops, functions, OOP, file handling, exception handling, modules, dan JSON persistence, lengkap dengan unit test (pytest).

## Urutan Belajar yang Disarankan

Ikuti urutan folder 01 → 10, kerjakan mini project setelah setiap kelompok topik selesai, lalu tutup dengan final project.
