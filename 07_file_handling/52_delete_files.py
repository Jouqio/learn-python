# 1. KONSEP

# Modul os dan shutil menyediakan fungsi untuk menghapus file dan folder.
#
# Fungsi yang sering digunakan:
# - os.remove(path)        → hapus satu file
# - os.rmdir(path)         → hapus folder KOSONG
# - shutil.rmtree(path)    → hapus folder beserta seluruh isinya (hati-hati!)
# - os.path.exists(path)   → cek apakah file/folder ada
# - os.listdir(path)       → daftar isi sebuah folder
#
# Penghapusan bersifat PERMANEN — tidak masuk ke Recycle Bin.

# 2. CONTOH

import os
import shutil

# Membuat file sementara untuk contoh
with open("sementara.txt", "w", encoding="utf-8") as f:
    f.write("isi sementara")

# Menghapus file — cek dulu sebelum hapus
if os.path.exists("sementara.txt"):
    os.remove("sementara.txt")
    print("sementara.txt berhasil dihapus.")
else:
    print("File tidak ditemukan.")

# Menghapus file dengan try/except — cara yang lebih aman
try:
    os.remove("tidak_ada.txt")
except FileNotFoundError:
    print("File tidak ditemukan — tidak ada yang dihapus.")

# Membuat dan menghapus folder kosong
os.mkdir("folder_kosong")
print(f"Folder dibuat: {os.path.exists('folder_kosong')}")  # True

os.rmdir("folder_kosong")
print(f"Folder dihapus: {os.path.exists('folder_kosong')}")  # False

# shutil.rmtree() — menghapus folder beserta isinya
# PERINGATAN: semua isi folder ikut terhapus secara permanen
os.mkdir("folder_berisi")
with open("folder_berisi/file1.txt", "w") as f:
    f.write("isi file 1")
with open("folder_berisi/file2.txt", "w") as f:
    f.write("isi file 2")

print(f"Isi folder: {os.listdir('folder_berisi')}")
shutil.rmtree("folder_berisi")  # hapus folder + semua isinya
print(f"Folder masih ada: {os.path.exists('folder_berisi')}")  # False

# os.listdir() — melihat isi folder sebelum menghapus
print(f"Isi direktori saat ini: {os.listdir('.')}")

# Contoh nyata: hapus semua kecuali 5 file terbaru
def bersihkan_log_lama(folder, simpan_terbaru=5):
    if not os.path.exists(folder):
        print(f"Folder '{folder}' tidak ditemukan.")
        return

    semua_file = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

    # Urutkan dari terbaru ke terlama berdasarkan waktu modifikasi
    semua_file.sort(key=os.path.getmtime, reverse=True)

    file_dihapus = semua_file[simpan_terbaru:]  # ambil yang di luar batas
    for file in file_dihapus:
        os.remove(file)
        print(f"Dihapus: {file}")

    print(f"Selesai — {len(file_dihapus)} file dihapus, {min(len(semua_file), simpan_terbaru)} file disimpan.")

# Uji fungsi dengan folder log
os.makedirs("logs", exist_ok=True)
for i in range(1, 9):
    with open(f"logs/log_{i}.txt", "w") as f:
        f.write(f"log {i}")

bersihkan_log_lama("logs", simpan_terbaru=5)
print(f"Sisa file: {os.listdir('logs')}")

# Bersihkan folder percobaan
shutil.rmtree("logs")

# 3. RANGKUMAN

# - os.remove()     → hapus satu file.
# - os.rmdir()      → hapus folder kosong saja.
# - shutil.rmtree() → hapus folder dan semua isinya (permanen, hati-hati).
# - Selalu cek os.path.exists() atau gunakan try/except sebelum menghapus.
# - os.listdir()    → lihat isi folder sebelum mengambil keputusan hapus.