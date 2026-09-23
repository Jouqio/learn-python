# 1. KONSEP

# Python memiliki dua cara menyimpan kumpulan data berurutan:
#
# list  → umum, bisa menyimpan berbagai tipe data sekaligus
# array → khusus data numerik bertipe sama, lebih hemat memori
#
# Modul array perlu diimpor terlebih dahulu.
# Kode tipe data yang sering dipakai:
# - "i" → integer (bilangan bulat)
# - "f" → float   (bilangan desimal)
# - "d" → double  (desimal presisi tinggi)

# 2. CONTOH

from array import array

# Membuat array bertipe integer
angka = array("i", [1, 2, 3, 4, 5])
print(angka)         # array('i', [1, 2, 3, 4, 5])

# Mengakses elemen lewat indeks
print(angka[0])      # 1
print(angka[-1])     # 5

# Mengubah nilai elemen
angka[0] = 10
print(angka)         # array('i', [10, 2, 3, 4, 5])

# Menambah elemen
angka.append(6)
print(angka)         # array('i', [10, 2, 3, 4, 5, 6])

# Iterasi dengan indeks
for i, nilai in enumerate(angka):
    print(f"indeks {i}: {nilai}")

# Menghitung rata-rata tanpa sum()
total = 0
for nilai in angka:
    total += nilai
rata_rata = total / len(angka)
print(f"Rata-rata: {rata_rata}")

# Konversi array ke list biasa
sebagai_list = list(angka)
print(sebagai_list)  # [10, 2, 3, 4, 5, 6]

# Array bertipe float
desimal = array("f", [1.1, 2.2, 3.3])
print(desimal)
print(sum(desimal) / len(desimal))

# Perbandingan list vs array
print("-- List: bisa campur tipe data --")
campur = [1, "dua", 3.0, True]
print(campur)

print("-- Array: hanya satu tipe data --")
# array("i", [1, "dua"])  # ini akan error

# 3. RANGKUMAN

# - list dipakai untuk data umum yang bisa campur tipe.
# - array dipakai khusus data numerik bertipe sama.
# - array lebih hemat memori dibanding list untuk data angka besar.
# - Gunakan "i" untuk integer, "f" untuk float saat membuat array.