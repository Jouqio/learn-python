# 1. KONSEP

# pip adalah alat bawaan Python untuk menginstal paket dari internet.
# Paket adalah kode yang dibuat orang lain dan bisa kita gunakan langsung.
#
# pip bekerja paling baik di dalam virtual environment (venv)
# agar setiap proyek punya dependensi yang terpisah dan tidak saling bentrok.

# 2. CONTOH

# Perintah pip dijalankan di TERMINAL, bukan di dalam file .py

# -- INSTALASI --
# pip install requests          → instal paket 'requests'
# pip install requests==2.31.0  → instal versi tertentu
# pip install -r requirements.txt → instal semua paket dari file

# -- MENGHAPUS --
# pip uninstall requests        → hapus paket

# -- MELIHAT PAKET TERINSTAL --
# pip list                      → tampilkan semua paket
# pip show requests             → detail satu paket

# -- MENYIMPAN DAFTAR PAKET --
# pip freeze > requirements.txt → ekspor semua paket ke file

# -- VIRTUAL ENVIRONMENT (sangat dianjurkan) --
# python -m venv venv           → buat virtual environment
# venv\Scripts\activate         → aktifkan (Windows)
# source venv/bin/activate      → aktifkan (Mac/Linux)
# deactivate                    → keluar dari virtual environment

print("Contoh setup proyek Python baru:")
print()
print("1. python -m venv venv")
print("2. venv\\Scripts\\activate  (Windows)")
print("3. pip install requests")
print("4. pip freeze > requirements.txt")

# Contoh isi requirements.txt yang dihasilkan:
readme = """
# Cara menjalankan proyek ini:

1. Buat virtual environment:
   python -m venv venv

2. Aktifkan virtual environment:
   Windows : venv\\Scripts\\activate
   Mac/Linux: source venv/bin/activate

3. Instal semua dependensi:
   pip install -r requirements.txt
"""
print(readme)

# 3. RANGKUMAN

# - pip digunakan untuk menginstal paket Python dari internet.
# - Selalu gunakan virtual environment (venv) agar proyek tidak saling bentrok.
# - Simpan daftar paket dengan: pip freeze > requirements.txt
# - Instal ulang dari daftar dengan: pip install -r requirements.txt