<h1 align="center">🐍 Python Learning</h1>

<p align="center">
  Belajar Python dari ZERO sampai ADVANCED dengan pendekatan bertahap dan project-based learning.
</p>

<p align="center">
  <b>Nama:</b> Syauqi Nuzul Adbi &nbsp;|&nbsp; <b>NIM:</b> 202512042
</p>

---

Kurikulum mengikuti urutan materi [W3Schools Python Tutorial](https://www.w3schools.com/python/)
sebagai referensi struktur belajar seluruh penjelasan, contoh kode, latihan, dan
mini project di repo ini ditulis ulang secara original.

## Tujuan
Membangun pemahaman Python secara bertahap: dari variabel dan tipe data,
sampai OOP, file handling, NumPy/Pandas/Matplotlib, machine learning dasar,
database, dan Django lalu menggabungkan semuanya dalam satu final project.

## Prerequisites
- Python 3.10 atau lebih baru (untuk fitur `match`)
- Visual Studio Code
- Koneksi internet untuk `pip install`

## Installation
```bash
git clone <your-fork-or-copy-of-this-repo> 
cd learn-python
python -m venv .venv
```

## VS Code Setup
1. Buka folder `python-learning-roadmap` di VS Code.
2. Install ekstensi **Python** (Microsoft) dan **Pylance**.
3. Pilih interpreter `.venv` melalui `Ctrl+Shift+P` → `Python: Select Interpreter`.

## Python Installation
Download dari [python.org](https://www.python.org/downloads/) jika belum
terinstall. Verifikasi dengan:
```bash
python --version
```

## Virtual Environment
```bash
# Buat
python -m venv .venv

# Aktivasi (Windows)
.venv\Scripts\activate

# Aktivasi (Linux/macOS)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Nonaktifkan
deactivate
```

## How to Run
Setiap file materi bisa langsung dijalankan:
```bash
python 01_fundamentals/01_home.py
```
Mini project dan final project punya `main.py` masing-masing:
```bash
python mini_projects/01_calculator/main.py
python projects/final_project/main.py
```

## Learning Roadmap
1. **Fundamentals** (`01_fundamentals/`) syntax dasar sampai operator
2. **Data Structures** (`02_data_structures/`) list, tuple, set, dict
3. **Control Flow** (`03_control_flow/`) if/else, match, loop
4. **Functions** (`04_functions/`) — function, lambda, scope, module
5. **Advanced Basics** (`05_advanced_basics/`) datetime, json, regex, try/except, venv
6. **OOP** (`06_oop/`) class, inheritance, polymorphism, encapsulation
7. **File Handling** (`07_file_handling/`) baca/tulis/hapus file
8. **Libraries** (`07_libraries/`) NumPy, Pandas, SciPy, Matplotlib
9. **Machine Learning** (`08_machine_learning/`) statistik dasar sampai KNN
10. **Database** (`09_database/`) MySQL & MongoDB
11. **Django** (`10_django/`) pengenalan web framework
12. **Mini Projects** (`mini_projects/`) 15 proyek kecil bertahap
13. **Final Project** (`projects/final_project/`) Student Management System

## Folder Structure
```
python-learning-roadmap/
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
│   ├── 01_calculator/ ... 15_expense_analyzer/
└── projects/
    └── final_project/
```

## Exercises
Setiap file topik (`01_....py` s/d `94_....py`) memiliki bagian
`3. PRACTICE` (3 easy + 2 medium) dan `4. CHALLENGE` di dalam file itu
sendiri. Latihan tambahan berdiri sendiri ada di `exercises/`, dengan
jawaban referensi di `solutions/`.

## Mini Projects
15 mini project bertahap di `mini_projects/`, dari kalkulator sederhana
sampai analisis data dengan pandas. Setiap project punya `README.md`,
`main.py`, dan `requirements.txt`.

## Final Project
`projects/final_project/` — **Student Management System**, menggabungkan
variables, data types, conditions, loops, functions, OOP, file handling,
exception handling, modules, dan JSON persistence dalam satu aplikasi CLI
lengkap dengan unit test (pytest).

## Clean Code Rules
- Ikuti PEP 8 dan gunakan penamaan yang jelas (bukan `x`, `y`, `z`)
- Function kecil, satu tanggung jawab (Single Responsibility)
- Hindari duplikasi kode (DRY) dan hard-coded value
- Selalu validasi input dan tangani error dengan try/except
- Kredensial database HANYA lewat environment variable, jangan hard-code

## Recommended Learning Order
Ikuti urutan folder 01 → 10, lalu kerjakan mini project setelah setiap
kelompok topik selesai, dan tutup dengan final project. Lihat `PROGRESS.md`
untuk checklist detail per topik.

## Progress Checklist
- [ ] Fundamentals (01_fundamentals)
- [ ] Data Structures (02_data_structures)
- [ ] Control Flow (03_control_flow)
- [ ] Functions (04_functions)
- [ ] Advanced Basics (05_advanced_basics)
- [ ] OOP (06_oop)
- [ ] File Handling (07_file_handling)
- [ ] NumPy / Pandas / SciPy / Matplotlib (07_libraries)
- [ ] Machine Learning (08_machine_learning)
- [ ] Database: MySQL & MongoDB (09_database)
- [ ] Django (10_django)
- [ ] Mini Projects (mini_projects)
- [ ] Final Project (projects/final_project)
