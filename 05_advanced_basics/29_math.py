# 1. KONSEP

# Modul math menyediakan fungsi dan konstanta matematika
# yang tidak tersedia di operator biasa.
#
# Tidak perlu instalasi — cukup import math.

# 2. CONTOH

import math

# Konstanta bawaan
print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045

# Pembulatan
print(math.ceil(4.1))   # 5 — bulatkan ke atas
print(math.floor(4.9))  # 4 — bulatkan ke bawah

# Akar dan pangkat
print(math.sqrt(144))   # 12.0 — akar kuadrat
print(math.pow(2, 8))   # 256.0 — pangkat (sama dengan 2 ** 8)

# Faktorial
print(math.factorial(5))  # 120 → 5 x 4 x 3 x 2 x 1

# Logaritma
print(math.log(100, 10))  # 2.0 — log basis 10
print(math.log2(8))       # 3.0 — log basis 2

# Hipotenusa segitiga siku-siku (teorema Pythagoras)
print(math.hypot(3, 4))   # 5.0 → √(3² + 4²)

# Contoh nyata: menghitung luas dan keliling lingkaran
def lingkaran(jari_jari):
    luas      = math.pi * jari_jari ** 2
    keliling  = 2 * math.pi * jari_jari
    print(f"Jari-jari : {jari_jari}")
    print(f"Luas      : {round(luas, 2)}")
    print(f"Keliling  : {round(keliling, 2)}")

lingkaran(7)

# 3. RANGKUMAN

# - import math untuk mengakses fungsi matematika tambahan.
# - math.sqrt() untuk akar, math.pow() untuk pangkat.
# - math.ceil() membulatkan ke atas, math.floor() ke bawah.
# - math.pi dan math.e adalah konstanta matematika yang sudah tersedia.