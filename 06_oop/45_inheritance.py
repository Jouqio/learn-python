# 1. KONSEP

# Inheritance memungkinkan sebuah class (anak) mewarisi atribut
# dan method dari class lain (induk), lalu memperluas atau mengubahnya.
#
# Manfaatnya:
# - Tidak perlu menulis ulang kode yang sama
# - Subclass bisa menambah atau mengubah perilaku induknya

# 2. CONTOH

# Class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return f"{self.nama} mengeluarkan suara."

    def info(self):
        return f"Nama: {self.nama}"

# Class anak — mewarisi Hewan
class Anjing(Hewan):
    def suara(self):                      # override method induk
        return f"{self.nama} menggonggong."

    def ambil_bola(self):                 # method baru, tidak ada di induk
        return f"{self.nama} mengambil bola!"

class Kucing(Hewan):
    def suara(self):                      # override method induk
        return f"{self.nama} mengeong."

# Menggunakan class induk dan anak
h  = Hewan("Hewan Generik")
a  = Anjing("Rex")
k  = Kucing("Mimi")

print(h.suara())        # Hewan Generik mengeluarkan suara.
print(a.suara())        # Rex menggonggong.
print(k.suara())        # Mimi mengeong.
print(a.ambil_bola())   # Rex mengambil bola!

# super() — memanggil method atau __init__ dari class induk
class HewanPeliharaan(Hewan):
    def __init__(self, nama, pemilik):
        super().__init__(nama)            # jalankan __init__ induk dulu
        self.pemilik = pemilik

    def info(self):
        return f"{super().info()}, Pemilik: {self.pemilik}"

hp = HewanPeliharaan("Buddy", "Andi")
print(hp.info())  # Nama: Buddy, Pemilik: Andi

# Polimorfisme — beberapa subclass diperlakukan seragam
daftar_hewan = [Anjing("Rex"), Kucing("Mimi"), Anjing("Bruno")]
for hewan in daftar_hewan:
    print(hewan.suara())   # setiap objek memanggil suara() versinya sendiri

# isinstance() dan issubclass() — mengecek hubungan pewarisan
print(isinstance(a, Anjing))   # True  — a adalah Anjing
print(isinstance(a, Hewan))    # True  — Anjing adalah turunan Hewan
print(issubclass(Anjing, Hewan))   # True
print(issubclass(Anjing, Kucing))  # False

# Contoh nyata: class Bentuk dengan beberapa subclass
import math

class Bentuk:
    def luas(self):
        return 0

    def info(self):
        return f"{self.__class__.__name__} — luas: {self.luas():.2f}"

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari ** 2

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

bentuk = [Lingkaran(7), Persegi(5), Lingkaran(3)]
for b in bentuk:
    print(b.info())

# 3. RANGKUMAN

# - Subclass mewarisi semua atribut dan method dari class induk.
# - Override method induk dengan menulis ulang method yang sama di subclass.
# - Gunakan super() untuk memanggil method atau __init__ dari class induk.
# - Polimorfisme memungkinkan banyak subclass diperlakukan seragam.
# - isinstance() mengecek tipe objek, issubclass() mengecek hubungan class.