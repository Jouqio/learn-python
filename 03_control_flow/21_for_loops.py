# 1. KONSEP

# For loop digunakan untuk mengulang kode sejumlah item
# dalam sebuah urutan (list, string, range, dictionary, dll.).
#
# Berbeda dengan while, for digunakan saat jumlah
# perulangan sudah diketahui atau mengikuti panjang data.

# 2. CONTOH

# For dengan range() — mengulang sejumlah angka
for i in range(1, 6):
    print(i)  # 1 2 3 4 5

# range(awal, akhir, langkah)
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# For dengan list
buah = ["apel", "pisang", "ceri"]
for item in buah:
    print(item)

# For dengan string — setiap karakter diiterasi satu per satu
for huruf in "Python":
    print(huruf)

# enumerate() — mengakses indeks dan nilai sekaligus
nama = ["Andi", "Bella", "Citra"]
for nomor, n in enumerate(nama, start=1):
    print(f"{nomor}. {n}")

# zip() — menggabungkan dua list secara bersamaan
siswa = ["Andi", "Bella", "Citra"]
nilai  = [90, 85, 92]
for n, v in zip(siswa, nilai):
    print(f"{n}: {v}")

# For dengan dictionary
profil = {"nama": "Bagas", "usia": 22, "kota": "Bontang"}
for kunci, nilai in profil.items():
    print(f"{kunci}: {nilai}")

# Nested for loop — loop di dalam loop
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris*kolom}", end="  ")
    print()  # baris baru setiap baris selesai

# 3. RANGKUMAN

# - for mengulang kode untuk setiap item dalam urutan.
# - range(awal, akhir, langkah) menghasilkan urutan angka.
# - enumerate() memberikan nomor urut otomatis saat iterasi.
# - zip() menggabungkan dua list menjadi pasangan.
# - Nested for loop digunakan untuk data dua dimensi seperti tabel.