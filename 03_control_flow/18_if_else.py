# 1. KONSEP

# Percabangan digunakan untuk menjalankan kode yang berbeda
# tergantung pada kondisi yang terpenuhi.
#
# Strukturnya:
# if kondisi:
#     jalankan ini jika kondisi True
# elif kondisi_lain:
#     jalankan ini jika kondisi pertama False
# else:
#     jalankan ini jika semua kondisi di atas False

# 2. CONTOH


# if / elif / else — menentukan grade dari nilai
nilai = 78

if nilai >= 90:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Grade: {grade}")  # Grade: B

# Mengecek genap atau ganjil
angka = 7
if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")

# Kondisi ganda dengan and / or
usia = 20
punya_ktp = True

if usia >= 17 and punya_ktp:
    print("Boleh membuat SIM.")
else:
    print("Tidak memenuhi syarat.")

# Nested if — if di dalam if
suhu = 35

if suhu > 0:
    if suhu >= 30:
        print("Panas")
    else:
        print("Sejuk")
else:
    print("Beku")

# Ternary — percabangan ringkas satu baris
stok = 10
status = "tersedia" if stok > 0 else "habis"
print(status)  # tersedia

# 3. RANGKUMAN

# - if menjalankan kode jika kondisi True.
# - elif menambah kondisi alternatif (boleh lebih dari satu).
# - else menangkap semua kondisi yang tidak terpenuhi.
# - Gunakan and/or untuk menggabungkan beberapa kondisi.
# - Ternary (x if kondisi else y) untuk percabangan sederhana satu baris.