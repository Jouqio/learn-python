# 1. KONSEP

# Ada dua jenis atribut di Python:
#
# - Atribut class    → dimiliki class, dibagi ke SEMUA objek
# - Atribut instance → dimiliki objek, UNIK untuk setiap objek
#
# Mengubah atribut class akan berdampak ke semua objek.
# Mengubah atribut instance hanya berdampak ke objek itu saja.

# 2. CONTOH

class Karyawan:
    perusahaan = "PT Nusantara Tech"   # atribut class — dibagi semua objek

    def __init__(self, nama, gaji):
        self.nama  = nama              # atribut instance — unik per objek
        self.gaji  = gaji

    def info(self):
        return f"{self.nama} — {self.perusahaan}"

k1 = Karyawan("Dian", 5000000)
k2 = Karyawan("Fikri", 6000000)

# Keduanya berbagi atribut class yang sama
print(k1.info())  # Dian — PT Nusantara Tech
print(k2.info())  # Fikri — PT Nusantara Tech

# Mengubah atribut class → berdampak ke SEMUA objek
Karyawan.perusahaan = "PT Digital Prima"
print(k1.info())  # Dian — PT Digital Prima
print(k2.info())  # Fikri — PT Digital Prima

# Mengubah atribut instance → hanya berdampak ke objek itu
k1.gaji = 5500000
print(k1.gaji)    # 5500000
print(k2.gaji)    # 6000000 — tidak berubah

# Menghitung jumlah objek yang dibuat lewat atribut class
class Produk:
    jumlah_produk = 0   # atribut class sebagai penghitung

    def __init__(self, nama, harga):
        self.nama  = nama
        self.harga = harga
        Produk.jumlah_produk += 1  # tambah setiap kali objek dibuat

p1 = Produk("Buku", 25000)
p2 = Produk("Pensil", 5000)
p3 = Produk("Tas", 150000)
print(f"Total produk terdaftar: {Produk.jumlah_produk}")  # 3

# @property — atribut yang dihitung otomatis, hanya bisa dibaca
class RekeningBank:
    nama_bank = "Bank Nusantara"   # atribut class

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo   = saldo

    @property
    def saldo_terformat(self):     # dipanggil seperti atribut, bukan method
        return f"Rp {self.saldo:,}"

    @property
    def info(self):
        return f"{self.pemilik} ({self.nama_bank}) — {self.saldo_terformat}"

rek = RekeningBank("Andi", 1500000)
print(rek.saldo_terformat)  # Rp 1,500,000
print(rek.info)             # Andi (Bank Nusantara) — Rp 1,500,000

# @property bersifat read-only — baris ini akan error jika dijalankan:
# rek.saldo_terformat = 999  # AttributeError

# 3. RANGKUMAN

# - Atribut class dibagi ke semua objek; ubah lewat NamaClass.atribut.
# - Atribut instance unik per objek; ubah lewat self.atribut.
# - Gunakan atribut class untuk data yang memang sama di semua objek.
# - Gunakan @property untuk atribut yang nilainya dihitung otomatis dari atribut lain.