# 1. KONSEP

# Enkapsulasi adalah cara menyembunyikan data internal dari akses luar,
# agar data hanya bisa diubah melalui cara yang sudah dikontrol.
#
# Konvensi penamaan di Python:
# - nama       → atribut publik, bebas diakses dari mana saja
# - _nama      → atribut terlindungi (protected), isyarat "jangan diakses dari luar"
# - __nama     → atribut privat, nama diubah Python agar sulit diakses langsung

# 2. CONTOH

# Atribut privat dengan __nama
class RekeningBank:
    def __init__(self, saldo):
        self.__saldo = saldo    # privat — tidak bisa diakses langsung dari luar

    # @property — getter, mengakses saldo secara read-only
    @property
    def saldo(self):
        return self.__saldo

    # @saldo.setter — setter dengan validasi
    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            print("Saldo tidak boleh negatif.")
        else:
            self.__saldo = nilai

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari nol.")
            return
        self.__saldo += jumlah
        print(f"Setor Rp {jumlah:,} → saldo: Rp {self.__saldo:,}")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup.")
            return
        self.__saldo -= jumlah
        print(f"Tarik Rp {jumlah:,} → saldo: Rp {self.__saldo:,}")

rek = RekeningBank(1000000)
rek.setor(500000)     # Setor Rp 500,000 → saldo: Rp 1,500,000
rek.tarik(200000)     # Tarik Rp 200,000 → saldo: Rp 1,300,000
print(rek.saldo)      # 1300000 — akses lewat @property

# Akses langsung ke atribut privat akan error
try:
    print(rek.__saldo)  # AttributeError
except AttributeError as e:
    print(f"Tidak bisa diakses langsung: {e}")

# Perbedaan publik, protected, dan privat
class Contoh:
    def __init__(self):
        self.publik     = "bebas diakses"       # publik
        self._terlindung = "sebaiknya tidak diakses dari luar"  # protected
        self.__privat   = "tidak bisa diakses langsung"         # privat

c = Contoh()
print(c.publik)       # bebas diakses
print(c._terlindung)  # bisa, tapi melanggar konvensi
# print(c.__privat)   # AttributeError

# Contoh nyata: class Password — tidak pernah membocorkan nilai asli
import hashlib

class Password:
    def __init__(self, kata_sandi):
        self.__hash = hashlib.sha256(kata_sandi.encode()).hexdigest()

    def cek(self, tebakan):
        return hashlib.sha256(tebakan.encode()).hexdigest() == self.__hash

pw = Password("rahasia123")
print(pw.cek("salah"))       # False
print(pw.cek("rahasia123"))  # True
# print(pw.__hash)           # AttributeError — tidak bisa diakses

# 3. RANGKUMAN

# - Enkapsulasi menyembunyikan data internal agar tidak diubah sembarangan.
# - Gunakan __nama untuk atribut privat yang tidak boleh diakses dari luar.
# - Gunakan @property untuk membuat getter yang aman (read-only).
# - Gunakan @nama.setter untuk mengontrol perubahan nilai dengan validasi.
# - _nama (satu garis bawah) hanya isyarat konvensi — Python tidak memblokir aksesnya.