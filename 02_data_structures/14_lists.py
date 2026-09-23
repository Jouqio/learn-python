# 1. KONSEP

# List adalah kumpulan data yang berurutan dan bisa diubah.
# Ditulis dengan tanda kurung siku: [item1, item2, item3]
#
# Sifat list:
# - Berurutan     → setiap item punya indeks mulai dari 0
# - Bisa diubah   → item bisa ditambah, dihapus, atau diganti
# - Boleh campur  → bisa menyimpan berbagai tipe data sekaligus

# 2. CONTOH

# Membuat list
buah = ["apel", "pisang", "ceri"]
print(buah)

# Mengakses item lewat indeks
print(buah[0])   # apel  (indeks pertama)
print(buah[-1])  # ceri  (indeks terakhir)

# Slicing — mengambil sebagian list
print(buah[0:2]) # ['apel', 'pisang']

# Menambah item
buah.append("kurma")     # tambah di akhir
buah.insert(1, "mangga") # tambah di indeks tertentu
print(buah)

# Menghapus item
buah.remove("pisang")  # hapus berdasarkan nilai
print(buah)

# Informasi list
print(len(buah))        # jumlah item
print(sorted(buah))     # diurutkan (tidak mengubah list asli)
print(sum([1, 2, 3]))   # total angka dalam list

# Mengubah nilai item
buah[0] = "anggur"
print(buah)

# Mengecek keanggotaan
print("apel" in buah)   # False — sudah diganti
print("anggur" in buah) # True

# List comprehension — cara ringkas membuat list baru
kuadrat = [n ** 2 for n in range(1, 6)]
print(kuadrat)  # [1, 4, 9, 16, 25]

# Filter dengan list comprehension
genap = [n for n in range(1, 11) if n % 2 == 0]
print(genap)  # [2, 4, 6, 8, 10]

# 3. RANGKUMAN

# - List menyimpan banyak nilai dalam satu variabel.
# - Gunakan .append() untuk menambah, .remove() untuk menghapus.
# - Indeks dimulai dari 0, indeks negatif dihitung dari belakang.
# - List comprehension membuat list baru dengan cara yang ringkas.