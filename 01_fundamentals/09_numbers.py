# 1. KONSEP

# Python mendukung tiga tipe angka:
#
# int     → bilangan bulat          contoh: 10, -5, 100
# float   → bilangan desimal        contoh: 3.14, -0.5
# complex → bilangan kompleks       contoh: 2+3j (jarang dipakai pemula)
#
# Fungsi bawaan yang berguna:
# - round(x, n) → membulatkan x ke n angka di belakang koma
# - abs(x)      → nilai mutlak (selalu positif)
# - pow(x, y)   → x pangkat y (sama dengan x ** y)

# 2. CONTOH

# Operasi dasar
print(10 + 3)   # penjumlahan → 13
print(10 - 3)   # pengurangan → 7
print(10 * 3)   # perkalian   → 30
print(10 / 3)   # pembagian   → 3.333...
print(10 // 3)  # pembagian bulat → 3
print(10 % 3)   # sisa bagi   → 1
print(2 ** 8)   # pangkat     → 256

# round(), abs(), pow()
print(round(3.14159, 2))  # 3.14
print(abs(-42))           # 42
print(pow(2, 10))         # 1024

# Contoh nyata: menghitung total belanja
harga = 19.999
jumlah = 3
total = round(harga * jumlah, 2)
print(f"Total belanja: Rp {total}")

# Konversi float ke int (angka di belakang koma dipotong, bukan dibulatkan)
print(int(9.9))   # 9, bukan 10

# 3. RANGKUMAN

# - int untuk bilangan bulat, float untuk desimal.
# - Gunakan // untuk pembagian bulat, % untuk sisa bagi.
# - Gunakan round() saat bekerja dengan uang atau nilai presisi.