# 1. KONSEP

# NumPy (Numerical Python) adalah library untuk mengolah data angka dengan cepat.
# Data disimpan dalam array (ndarray), yang jauh lebih cepat daripada list biasa.
#
# Instalasi: pip install numpy
#
# Hal-hal yang dibahas:
# np.array()        → membuat array
# arr[indeks]       → mengambil elemen (indexing)
# arr[awal:akhir]   → mengambil sebagian elemen (slicing)
# dtype             → tipe data array
# copy() dan view() → menyalin array
# shape, reshape()  → bentuk array dan mengubah bentuknya
# np.concatenate()  → menggabungkan array
# np.array_split()  → membagi array
# np.where()        → mencari posisi nilai
# np.sort()         → mengurutkan array
# arr[arr > 4]      → menyaring (filter) array
# default_rng()     → membuat angka acak

# 2. CONTOH

import numpy as np

# Membuat array
angka = np.array([1, 2, 3, 4, 5])
print("Array:", angka)
print("Tipe:", type(angka))

# Indexing — mengambil satu elemen
matriks = np.array([[1, 2, 3], [4, 5, 6]])
print("Baris 1, kolom 2:", matriks[1, 2])

# Slicing — mengambil sebagian elemen
print("Baris pertama:", matriks[0, :])
print("Baris 0-1, kolom 1-2:\n", matriks[0:2, 1:3])

# Tipe data
angka_desimal = np.array([1, 2, 3], dtype="f")
print("Tipe data:", angka_desimal.dtype)

# Copy dan view
asli = np.array([10, 20, 30])
tampilan = asli.view()    # ikut berubah jika array asli berubah
salinan = asli.copy()     # tidak terpengaruh array asli
asli[0] = 999
print("Asli:", asli)
print("View:", tampilan)
print("Copy:", salinan)

# Shape dan reshape
datar = np.array([1, 2, 3, 4, 5, 6])
print("Shape:", datar.shape)

bentuk_baru = datar.reshape(2, 3)    # 2 baris, 3 kolom
print("Setelah reshape:\n", bentuk_baru)

# Iterasi (perulangan)
for baris in bentuk_baru:
    for nilai in baris:
        print("Nilai:", nilai)

# Menggabungkan dan membagi array
a = np.array([1, 2])
b = np.array([3, 4])

gabungan = np.concatenate((a, b))
print("Gabungan:", gabungan)

hasil_bagi = np.array_split(gabungan, 2)
print("Dibagi dua:", hasil_bagi)

# Mencari, mengurutkan, dan menyaring
data = np.array([5, 2, 9, 1, 5, 6])

print("Posisi nilai 9:", np.where(data == 9))
print("Terurut:", np.sort(data))
print("Nilai lebih dari 4:", data[data > 4])

# Angka acak
acak = np.random.default_rng(seed=42)
print("Desimal acak:", acak.random(3))
print("Bilangan bulat acak 1-10:", acak.integers(1, 11, size=5))

# 3. RANGKUMAN

# - np.array() membuat array, dan array lebih cepat daripada list untuk data angka.
# - Indexing dan slicing memakai [baris, kolom] untuk mengambil elemen.
# - copy() membuat salinan mandiri, view() ikut berubah jika array asli berubah.
# - shape menunjukkan bentuk array, reshape() mengubah bentuknya.
# - np.concatenate() menggabungkan, np.array_split() membagi array.
# - np.where() mencari posisi, np.sort() mengurutkan, arr[arr > 4] menyaring data.
# - default_rng() dengan seed membuat angka acak yang hasilnya bisa diulang.