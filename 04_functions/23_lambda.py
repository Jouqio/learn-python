# 1. KONSEP

# Lambda adalah fungsi kecil tanpa nama yang ditulis dalam satu baris.
# Berguna untuk operasi singkat yang tidak perlu dibuat fungsi penuh.
#
# Sintaks:
# lambda parameter: ekspresi
#
# Kapan pakai lambda:
# - Sebagai argumen sorted(), map(), filter()
# - Logika sederhana yang hanya dipakai sekali

# 2. CONTOH

# Lambda dasar
kuadrat = lambda x: x ** 2
print(kuadrat(5))   # 25

# Perbandingan lambda vs fungsi biasa — keduanya identik
def kuadrat_def(x):
    return x ** 2

# sorted() dengan lambda — menentukan aturan pengurutan
angka = [5, 2, 8, 1, 9]
print(sorted(angka))                          # urutan naik (default)
print(sorted(angka, key=lambda n: -n))        # urutan turun

# Mengurutkan list of tuple berdasarkan elemen kedua
siswa = [("Andi", 90), ("Budi", 75), ("Citra", 85)]
print(sorted(siswa, key=lambda s: s[1]))      # urut dari nilai terkecil

# Mengurutkan list of dictionary berdasarkan harga
produk = [
    {"nama": "Buku",   "harga": 25000},
    {"nama": "Pensil", "harga": 5000},
    {"nama": "Tas",    "harga": 150000},
]
print(sorted(produk, key=lambda p: p["harga"]))

# map() — menerapkan fungsi ke setiap item dalam list
kata = ["halo", "python", "dunia"]
print(list(map(lambda k: k.upper(), kata)))   # ['HALO', 'PYTHON', 'DUNIA']

# filter() — menyaring item yang memenuhi kondisi
angka = [5, -3, 8, -1, 9, -6]
print(list(filter(lambda n: n > 0, angka)))   # [5, 8, 9]

# 3. RANGKUMAN

# - Lambda adalah fungsi satu baris tanpa nama: lambda x: x * 2
# - Cocok dipakai sebagai argumen sorted(), map(), filter().
# - Untuk logika yang lebih kompleks, gunakan def — lebih mudah dibaca.