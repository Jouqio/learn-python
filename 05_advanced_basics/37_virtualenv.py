# 1. KONSEP

# Virtual environment adalah folder terisolasi yang menyimpan
# paket khusus untuk satu proyek saja.
#
# Tanpa venv → semua proyek berbagi paket yang sama → bisa konflik
# Dengan venv → setiap proyek punya paket sendiri → aman dan rapi
#
# Kapan butuh venv:
# - Setiap kali memulai proyek Python baru
# - Saat proyek butuh versi paket yang berbeda-beda

# 2. CONTOH

# Semua perintah di bawah dijalankan di TERMINAL, bukan di dalam file .py

# -- MEMBUAT DAN MENGAKTIFKAN --
# python -m venv .venv              → buat virtual environment
# .venv\Scripts\activate            → aktifkan (Windows)
# source .venv/bin/activate         → aktifkan (Mac/Linux)
# deactivate                        → keluar dari virtual environment

# -- MENGELOLA PAKET DI DALAM VENV --
# pip install requests              → instal paket
# pip freeze > requirements.txt     → simpan daftar paket
# pip install -r requirements.txt   → instal dari daftar

print("Panduan setup proyek Python dari awal:")
print()
print("1. Buat virtual environment  : python -m venv .venv")
print("2. Aktifkan (Windows)        : .venv\\Scripts\\activate")
print("3. Aktifkan (Mac/Linux)      : source .venv/bin/activate")
print("4. Instal paket yang dibutuhkan: pip install -r requirements.txt")
print("5. Selesai, mulai koding!")
print()
print("Jika mau keluar dari venv    : deactivate")

# Panduan lengkap untuk kontributor baru
panduan = """
=== PANDUAN SETUP UNTUK KONTRIBUTOR BARU ===

1. Clone repositori:
   git clone https://github.com/username/nama-repo.git
   cd nama-repo

2. Buat virtual environment:
   python -m venv .venv

3. Aktifkan virtual environment:
   Windows  : .venv\\Scripts\\activate
   Mac/Linux: source .venv/bin/activate

4. Instal semua dependensi:
   pip install -r requirements.txt

5. Jalankan skrip pertama:
   python 01_fundamentals/01_home.py

Selamat belajar!
"""
print(panduan)

# 3. RANGKUMAN

# - Gunakan venv di setiap proyek agar paket tidak saling bentrok.
# - Buat dengan: python -m venv .venv
# - Aktifkan sebelum install paket apa pun.
# - Simpan daftar paket dengan: pip freeze > requirements.txt
# - Tambahkan folder .venv ke dalam .gitignore — jangan di-commit.