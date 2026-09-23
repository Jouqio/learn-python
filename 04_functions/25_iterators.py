# 1. KONSEP

# Iterator adalah objek yang bisa menghasilkan nilai satu per satu
# menggunakan fungsi next().
#
# Perbedaan iterable dan iterator:
# - Iterable → bisa diulang (list, string, range) tapi belum tentu iterator
# - Iterator  → objek yang punya next(), dihasilkan dari iter()
#
# Di balik layar, for loop Python sebenarnya menggunakan iterator secara otomatis.

# 2. CONTOH

# Membuat iterator dari list
angka = [10, 20, 30]
it = iter(angka)        # ubah list menjadi iterator

print(next(it))         # 10
print(next(it))         # 20
print(next(it))         # 30
# next(it) lagi → StopIteration (data habis)

# Menangani StopIteration dengan try/except
it2 = iter([1, 2])
try:
    print(next(it2))    # 1
    print(next(it2))    # 2
    print(next(it2))    # memicu StopIteration
except StopIteration:
    print("Data iterator sudah habis.")

# For loop = iterator secara otomatis di balik layar
for n in [10, 20, 30]:
    print(n)
# Kode di atas setara dengan menggunakan iter() + next() secara manual

# Generator expression — iterator ringkas dan hemat memori
kuadrat = (n ** 2 for n in range(1, 6))  # pakai () bukan []
for nilai in kuadrat:
    print(nilai)        # 1 4 9 16 25

# Kelas iterator kustom — membuat countdown sendiri
class HitungMundur:
    def __init__(self, mulai):
        self.angka = mulai

    def __iter__(self):
        return self

    def __next__(self):
        if self.angka <= 0:
            raise StopIteration
        self.angka -= 1
        return self.angka + 1

for n in HitungMundur(5):
    print(n)            # 5 4 3 2 1

# Kelas iterator kustom — bilangan genap sampai batas tertentu
class BilanganGenap:
    def __init__(self, batas):
        self.angka = 0
        self.batas = batas

    def __iter__(self):
        return self

    def __next__(self):
        self.angka += 2
        if self.angka > self.batas:
            raise StopIteration
        return self.angka

for n in BilanganGenap(10):
    print(n)            # 2 4 6 8 10

# 3. RANGKUMAN

# - Iterable adalah objek yang bisa diulang (list, string, range).
# - Iterator dihasilkan dari iter() dan menggunakan next() untuk ambil nilai.
# - For loop menggunakan iterator secara otomatis di balik layar.
# - Generator expression (...) membuat iterator ringkas tanpa kelas.
# - Buat iterator kustom dengan mengimplementasikan __iter__ dan __next__.