# 1. KONSEP

# Boolean hanya punya dua nilai: True (benar) atau False (salah).
# Dihasilkan dari operasi perbandingan dan digunakan untuk pengambilan keputusan.
#
# Operator boolean:
# - and → keduanya harus True
# - or  → salah satu cukup True
# - not → membalik nilai (True jadi False, sebaliknya)
#
# Nilai yang dianggap False (falsy):
# - 0, 0.0, "", [], {}, None

# 2. CONTOH

# Nilai boolean dasar
sudah_login = True
punya_izin  = False

# Operator and, or, not
print(sudah_login and punya_izin)   # False — keduanya harus True
print(sudah_login or punya_izin)    # True  — salah satu cukup
print(not sudah_login)              # False — dibalik

# Hasil perbandingan menghasilkan boolean
print(5 > 3)    # True
print(5 == 3)   # False
print(5 != 3)   # True

# Truthiness — nilai non-boolean yang dianggap True atau False
print(bool(""))     # False — string kosong
print(bool("teks")) # True  — string berisi
print(bool(0))      # False — angka nol
print(bool([1, 2])) # True  — list berisi

# Contoh nyata: mengecek kondisi ganda
usia = 20
warga_negara = True

boleh_memilih = usia >= 17 and warga_negara
print(boleh_memilih)  # True

# 3. RANGKUMAN

# - Boolean hanya True atau False.
# - Gunakan and, or, not untuk menggabungkan kondisi.
# - Nilai kosong (0, "", [], None) dianggap False oleh Python.