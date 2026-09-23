# 1. KONSEP

# Python memiliki beberapa tipe data bawaan yang sering digunakan:
#
# str   → teks              contoh: "halo"
# int   → bilangan bulat    contoh: 10
# float → bilangan desimal  contoh: 3.14
# bool  → benar/salah       contoh: True, False
# list  → daftar            contoh: [1, 2, 3]
# tuple → daftar tetap      contoh: (1, 2, 3)
# dict  → pasangan kunci-nilai  contoh: {"nama": "Aulia"}
# set   → kumpulan unik     contoh: {1, 2, 3}
#
# Gunakan type() untuk mengecek tipe data sebuah nilai.

# 2. CONTOH

# Mencetak tipe data dari berbagai nilai
nilai = ["teks", 10, 3.14, True, [1, 2], (1, 2), {"a": 1}, {1, 2}]
for item in nilai:
    print(item, "->", type(item).__name__)

# Mengecek tipe data dengan isinstance()
angka = 42
print(isinstance(angka, int))    # True
print(isinstance(angka, float))  # False

# 3. RANGKUMAN

# - Python punya banyak tipe data bawaan untuk berbagai kebutuhan.
# - Gunakan type() untuk melihat tipe sebuah nilai.
# - Gunakan isinstance() untuk mengecek apakah nilai bertipe tertentu.