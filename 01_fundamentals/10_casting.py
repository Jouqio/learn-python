# 1. KONSEP

# Konversi tipe data adalah mengubah nilai dari satu tipe ke tipe lain.
#
# Fungsi yang digunakan:
# - int()   → mengubah ke bilangan bulat
# - float() → mengubah ke bilangan desimal
# - str()   → mengubah ke teks
# - bool()  → mengubah ke True/False

# 2. CONTOH

# str ke int — sering terjadi saat memproses input pengguna
usia_teks = "25"
usia_angka = int(usia_teks)
print(usia_angka + 5)          # 30
print(str(usia_angka) + " tahun")  # 25 tahun

# str ke float
nilai_teks = "3.14"
nilai_float = float(nilai_teks)
print(nilai_float)             # 3.14

# float ke int — angka di belakang koma dipotong
print(int(9.99))               # 9

# int ke bool
print(bool(0))    # False
print(bool(1))    # True
print(bool(99))   # True

# Konversi aman dengan try/except
# (mencegah program crash jika nilai tidak bisa dikonversi)
teks = "abc"
try:
    angka = int(teks)
except ValueError:
    angka = 0
print(angka)  # 0

# 3. RANGKUMAN

# - Gunakan int(), float(), str(), bool() untuk mengubah tipe data.
# - float ke int memotong desimal, bukan membulatkan.
# - Gunakan try/except saat mengonversi input dari pengguna
#   agar program tidak crash jika nilainya tidak valid.