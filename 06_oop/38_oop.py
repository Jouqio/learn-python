# 1. KONSEP

# OOP (Object-Oriented Programming) adalah cara mengorganisasi kode
# menggunakan "objek" yang menggabungkan data (atribut) dan perilaku (method).
#
# Istilah penting:
# - Class  → cetakan/blueprint untuk membuat objek
# - Objek  → hasil nyata dari sebuah class (instance)
# - Atribut → data yang dimiliki objek (seperti variabel)
# - Method  → fungsi yang dimiliki objek

# 2. CONTOH

# Membuat class
class Buku:
    def __init__(self, judul, penulis):
        self.judul   = judul    # atribut
        self.penulis = penulis  # atribut

    def deskripsi(self):        # method
        return f"{self.judul} oleh {self.penulis}"

# Membuat objek (instance) dari class Buku
buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")

# Memanggil method
print(buku1.deskripsi())  # Laskar Pelangi oleh Andrea Hirata
print(buku2.deskripsi())  # Bumi Manusia oleh Pramoedya Ananta Toer

# Mengakses atribut langsung
print(buku1.judul)   # Laskar Pelangi
print(buku2.penulis) # Pramoedya Ananta Toer

# Contoh nyata: class Produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama  = nama
        self.harga = harga
        self.stok  = stok

    def tersedia(self):
        return self.stok > 0

    def info(self):
        status = "tersedia" if self.tersedia() else "habis"
        return f"{self.nama} — Rp {self.harga:,} ({status})"

    def beli(self, jumlah):
        if jumlah > self.stok:
            print("Stok tidak cukup.")
        else:
            self.stok -= jumlah
            print(f"{jumlah} {self.nama} berhasil dibeli.")

# Membuat dan menggunakan objek Produk
laptop = Produk("Laptop", 8500000, 5)
print(laptop.info())  # Laptop — Rp 8,500,000 (tersedia)

laptop.beli(2)
print(f"Sisa stok: {laptop.stok}")  # 3

# 3. RANGKUMAN

# - Class adalah cetakan; objek adalah hasil nyata dari cetakan itu.
# - Atribut menyimpan data objek, method mendefinisikan perilakunya.
# - Satu class bisa menghasilkan banyak objek dengan data berbeda.
# - OOP membuat kode lebih terstruktur dan mudah dikembangkan.