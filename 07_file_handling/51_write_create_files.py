# 1. KONSEP

# Tiga mode penulisan file di Python:
#
# - "w" → tulis ulang — membuat file baru atau MENIMPA isi lama
# - "a" → tambah — menulis di akhir file TANPA menghapus isi lama
# - "x" → buat eksklusif — error jika file sudah ada
#
# Pilih mode yang tepat agar tidak kehilangan data secara tidak sengaja.

# 2. CONTOH

# Mode "w" — membuat file baru atau menimpa yang sudah ada
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

# Mode "a" — menambah di akhir tanpa menghapus isi sebelumnya
with open("catatan.txt", "a", encoding="utf-8") as f:
    f.write("Baris ketiga\n")

# Verifikasi isi file
with open("catatan.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Mode "x" — hanya membuat jika file belum ada
try:
    with open("baru.txt", "x", encoding="utf-8") as f:
        f.write("File baru berhasil dibuat.\n")
except FileExistsError:
    print("File sudah ada — mode 'x' dibatalkan.")

# Menulis list ke file — satu item per baris
daftar_nama = ["Andi", "Budi", "Citra", "Dewi"]

with open("nama.txt", "w", encoding="utf-8") as f:
    for nama in daftar_nama:
        f.write(nama + "\n")

with open("nama.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Menulis laporan terformat dengan f-string
data_siswa = [
    ("Andi",  90, "Lulus"),
    ("Budi",  55, "Tidak Lulus"),
    ("Citra", 78, "Lulus"),
]

with open("laporan.txt", "w", encoding="utf-8") as f:
    f.write("=== LAPORAN NILAI SISWA ===\n\n")
    for nama, nilai, status in data_siswa:
        f.write(f"{nama:<10} | Nilai: {nilai} | {status}\n")

with open("laporan.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Contoh nyata: fungsi append_log dengan timestamp
from datetime import datetime

def catat_log(nama_file, pesan):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(nama_file, "a", encoding="utf-8") as f:
        f.write(f"[{waktu}] {pesan}\n")

catat_log("app.log", "Program dimulai.")
catat_log("app.log", "Pengguna login.")
catat_log("app.log", "Program selesai.")

with open("app.log", "r", encoding="utf-8") as f:
    print(f.read())

# 3. RANGKUMAN

# - "w" menimpa seluruh isi file — hati-hati, data lama hilang.
# - "a" menambah di akhir file — aman untuk log dan data bertahap.
# - "x" membuat file baru saja — gagal jika file sudah ada.
# - Gunakan writelines() atau loop untuk menulis banyak baris sekaligus.