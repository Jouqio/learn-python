# 1. KONSEP

# Polimorfisme artinya "banyak bentuk" — beberapa class berbeda
# bisa diperlakukan sama karena punya method dengan nama yang sama.
#
# Manfaatnya:
# - Kode tidak perlu tahu jenis objek secara spesifik
# - Tidak perlu banyak if/elif untuk mengecek tipe objek

# 2. CONTOH

# Polimorfisme dasar — class berbeda, method nama sama
class Kucing:
    def suara(self):
        return "Meong"

class Bebek:
    def suara(self):
        return "Kwek"

class Sapi:
    def suara(self):
        return "Moo"

# Semua diperlakukan sama — tidak perlu cek tipe objek
hewan = [Kucing(), Bebek(), Sapi()]
for h in hewan:
    print(h.suara())   # setiap objek tahu suaranya sendiri

# Polimorfisme bawaan Python — len() bekerja di banyak tipe
print(len("Python"))        # 6   — string
print(len([1, 2, 3]))       # 3   — list
print(len({"a": 1, "b": 2}))  # 2 — dictionary

# Fungsi yang menerima objek apa saja selama punya method yang dibutuhkan
def cetak_suara(objek):
    print(objek.suara())   # tidak peduli tipe objeknya

cetak_suara(Kucing())  # Meong
cetak_suara(Bebek())   # Kwek

# Polimorfisme lewat inheritance — subclass override method induk
class Bentuk:
    def luas(self):
        return 0

    def info(self):
        return f"{self.__class__.__name__}: luas = {self.luas():.2f}"

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r

    def luas(self):
        import math
        return math.pi * self.r ** 2

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class SegitigaSiku(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas   = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

# Fungsi yang bekerja untuk semua subclass Bentuk
def total_luas(daftar_bentuk):
    return sum(b.luas() for b in daftar_bentuk)

bentuk = [Lingkaran(7), Persegi(5), SegitigaSiku(6, 4)]

for b in bentuk:
    print(b.info())

print(f"Total luas: {total_luas(bentuk):.2f}")

# 3. RANGKUMAN

# - Polimorfisme memungkinkan objek berbeda diperlakukan dengan cara yang sama.
# - Cukup pastikan setiap class punya method dengan nama yang sama.
# - Kode yang memanggil method tidak perlu tahu jenis objeknya (tidak perlu if/elif tipe).
# - Python mendukung polimorfisme secara alami — len(), print(), dll. sudah polimorfik.