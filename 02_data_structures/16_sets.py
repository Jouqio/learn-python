# 1. KONSEP

# Set adalah kumpulan data yang:
# - Tidak berurutan → tidak ada indeks
# - Tidak boleh duplikat → nilai yang sama hanya disimpan sekali
# Ditulis dengan tanda kurung kurawal: {item1, item2, item3}
#
# Kegunaan utama set:
# - Menghapus duplikat dari sebuah list
# - Mengecek keanggotaan dengan cepat
# - Operasi himpunan: gabungan, irisan, selisih

# 2. CONTOH

# Membuat set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Set otomatis hapus duplikat
angka = {1, 2, 2, 3, 3, 3}
print(angka)  # {1, 2, 3}

# Menambah dan menghapus item
a.add(10)
print(a)            # {1, 2, 3, 4, 10}

a.discard(10)       # hapus item — tidak error jika tidak ada
print(a)            # {1, 2, 3, 4}

# Mengecek keanggotaan
print(3 in a)       # True
print(9 in a)       # False

# Operasi himpunan
print(a | b)        # gabungan   → semua item dari a dan b
print(a & b)        # irisan     → item yang ada di keduanya
print(a - b)        # selisih    → item di a yang tidak ada di b

# Menghapus duplikat dari list menggunakan set
daftar = ["apel", "pisang", "apel", "ceri", "pisang"]
unik = list(set(daftar))
print(unik)

# Contoh nyata: mencari email yang terdaftar di dua daftar
daftar_a = {"andi@mail.com", "budi@mail.com", "cici@mail.com"}
daftar_b = {"budi@mail.com", "dedi@mail.com", "cici@mail.com"}

ada_di_keduanya = daftar_a & daftar_b
print(ada_di_keduanya)  # {'budi@mail.com', 'cici@mail.com'}

# 3. RANGKUMAN

# - Set tidak menyimpan duplikat dan tidak berurutan.
# - Gunakan set untuk menghapus duplikat dari list.
# - Operasi himpunan: | (gabungan), & (irisan), - (selisih).
# - Gunakan .add() untuk menambah, .discard() untuk menghapus.