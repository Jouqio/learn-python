# 1. KONSEP

# Regular expression (regex) adalah pola teks untuk mencari,
# memvalidasi, atau mengganti string.
# Diakses lewat modul re (sudah bawaan Python).
#
# Fungsi utama:
# - re.search()    → cari pola, kembalikan match pertama
# - re.findall()   → cari semua kecocokan, kembalikan list
# - re.sub()       → ganti teks yang cocok dengan pola
# - re.fullmatch() → cek apakah seluruh string cocok dengan pola
# - re.split()     → pecah string berdasarkan pola
#
# Simbol pola yang sering dipakai:
# \d  → satu angka (0-9)
# \w  → huruf, angka, atau underscore
# \s  → spasi atau tab
# .   → karakter apa saja (kecuali newline)
# +   → satu atau lebih
# *   → nol atau lebih
# ?   → nol atau satu (opsional)
# []  → salah satu karakter di dalam kurung

# 2. CONTOH

import re

teks = "Hubungi: budi@email.com atau 0812-3456-7890"

# findall() — mencari semua kecocokan
email = re.findall(r"[\w.]+@[\w.]+", teks)
print(email)   # ['budi@email.com']

# sub() — mengganti teks yang cocok
disensor = re.sub(r"\d", "#", teks)
print(disensor)  # Hubungi: budi@email.com atau ####-####-####

# search() — cari kecocokan pertama
cocok = re.search(r"\d{4}", teks)
if cocok:
    print(f"Angka pertama yang ditemukan: {cocok.group()}")  # 0812

# fullmatch() — validasi format seluruh string
def validasi_kode_pos(kode):
    return bool(re.fullmatch(r"\d{5}", kode))

print(validasi_kode_pos("75311"))  # True  — 5 digit angka
print(validasi_kode_pos("7531A"))  # False — ada huruf

# split() — memecah string berdasarkan beberapa pemisah
kalimat = "apel,pisang;mangga,ceri;nanas"
buah = re.split(r"[,;]", kalimat)  # pecah di koma atau titik koma
print(buah)   # ['apel', 'pisang', 'mangga', 'ceri', 'nanas']

# Contoh nyata: validasi nomor HP Indonesia (08xx-xxxx-xxxx)
def validasi_nomor_hp(nomor):
    pola = r"08\d{2}-\d{4}-\d{4}"
    return bool(re.fullmatch(pola, nomor))

print(validasi_nomor_hp("0812-3456-7890"))  # True
print(validasi_nomor_hp("08123456789"))     # False — tanpa tanda hubung
print(validasi_nomor_hp("0712-3456-7890"))  # False — tidak diawali 08

# Ekstrak semua hashtag dari caption media sosial
caption = "Belajar #Python itu seru! #KodingIndonesia #pemula"
hashtag = re.findall(r"#\w+", caption)
print(hashtag)  # ['#Python', '#KodingIndonesia', '#pemula']

# 3. RANGKUMAN

# - Regex digunakan untuk mencari, memvalidasi, dan mengganti pola teks.
# - Gunakan findall() untuk semua kecocokan, search() untuk yang pertama.
# - Gunakan sub() untuk mengganti, fullmatch() untuk validasi format penuh.
# - Pola ditulis di dalam r"..." (raw string) agar backslash tidak salah diartikan.