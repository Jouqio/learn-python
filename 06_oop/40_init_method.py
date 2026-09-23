# 1. KONSEP

# __init__ adalah method khusus yang otomatis dipanggil
# saat objek baru dibuat dari sebuah class.
# Digunakan untuk mengatur nilai awal atribut objek.
#
# __init__ bukan class itu sendiri — ia hanya bagian dari class
# yang berjalan sekali di awal saat objek dibuat.

# 2. CONTOH

# __init__ dasar
class Akun:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo   = saldo

    def info(self):
        return f"Akun milik {self.pemilik} — saldo: Rp {self.saldo:,}"

akun1 = Akun("Rina")           # saldo pakai default: 0
akun2 = Akun("Budi", 500000)   # saldo diisi manual

print(akun1.info())  # Akun milik Rina — saldo: Rp 0
print(akun2.info())  # Akun milik Budi — saldo: Rp 500,000

# __init__ dengan validasi — mencegah data tidak valid sejak awal
class Persegi:
    def __init__(self, lebar, tinggi):
        if lebar <= 0 or tinggi <= 0:
            raise ValueError("Lebar dan tinggi harus lebih dari nol.")
        self.lebar  = lebar
        self.tinggi = tinggi

    def luas(self):
        return self.lebar * self.tinggi

    def keliling(self):
        return 2 * (self.lebar + self.tinggi)

p = Persegi(5, 3)
print(f"Luas     : {p.luas()}")      # 15
print(f"Keliling : {p.keliling()}")  # 16

# Mencoba membuat objek dengan nilai tidak valid
try:
    p2 = Persegi(-5, 3)
except ValueError as e:
    print(f"Error: {e}")

# Atribut yang dihitung otomatis di __init__
class Lingkaran:
    def __init__(self, jari_jari):
        import math
        self.jari_jari = jari_jari
        self.luas      = round(math.pi * jari_jari ** 2, 2)  # dihitung saat dibuat
        self.keliling  = round(2 * math.pi * jari_jari, 2)

l = Lingkaran(7)
print(f"Jari-jari: {l.jari_jari}")
print(f"Luas     : {l.luas}")
print(f"Keliling : {l.keliling}")

# 3. RANGKUMAN

# - __init__ dipanggil otomatis saat objek dibuat.
# - Gunakan __init__ untuk mengatur nilai awal atribut.
# - Parameter bisa diberi nilai default agar opsional.
# - Letakkan validasi di dalam __init__ agar objek selalu punya data yang valid.