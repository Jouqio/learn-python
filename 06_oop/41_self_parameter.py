# 1. KONSEP

# self adalah cara sebuah method merujuk ke objeknya sendiri.
# Dengan self, method bisa mengakses dan mengubah atribut milik objek itu.
#
# Aturan self:
# - Selalu menjadi parameter pertama di setiap method
# - Tidak perlu diisi saat memanggil method — Python mengisinya otomatis
# - Nama "self" adalah konvensi, tapi sangat dianjurkan untuk konsistensi

# 2. CONTOH

# self merujuk ke objek yang sedang memanggil method tersebut
class Penghitung:
    def __init__(self):
        self.jumlah = 0        # atribut milik objek ini

    def tambah(self):
        self.jumlah += 1       # mengubah atribut lewat self

    def reset(self):
        self.jumlah = 0

    def info(self):
        return f"Jumlah saat ini: {self.jumlah}"

    def tambah_dan_info(self):
        self.tambah()          # method memanggil method lain lewat self
        return self.info()

c = Penghitung()
c.tambah()
c.tambah()
print(c.info())               # Jumlah saat ini: 2
print(c.tambah_dan_info())    # Jumlah saat ini: 3

# Setiap objek punya self (data) yang TERPISAH
c1 = Penghitung()
c2 = Penghitung()

c1.tambah()
c1.tambah()
c2.tambah()

print(c1.jumlah)  # 2 — milik c1
print(c2.jumlah)  # 1 — milik c2, tidak terpengaruh c1

# Contoh nyata: class Dompet
class Dompet:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.saldo   = saldo_awal

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari nol.")
            return
        self.saldo += jumlah
        print(f"Setor Rp {jumlah:,} → saldo: Rp {self.saldo:,}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup.")
            return
        self.saldo -= jumlah
        print(f"Tarik Rp {jumlah:,} → saldo: Rp {self.saldo:,}")

    def info(self):
        return f"Dompet {self.pemilik}: Rp {self.saldo:,}"

dompet = Dompet("Andi", 100000)
dompet.setor(50000)   # Setor Rp 50,000 → saldo: Rp 150,000
dompet.tarik(30000)   # Tarik Rp 30,000 → saldo: Rp 120,000
dompet.tarik(200000)  # Saldo tidak cukup.
print(dompet.info())  # Dompet Andi: Rp 120,000

# 3. RANGKUMAN

# - self merujuk ke objek yang sedang menggunakan method tersebut.
# - Setiap method harus punya self sebagai parameter pertama.
# - Lewat self, method bisa membaca dan mengubah atribut objeknya sendiri.
# - Setiap objek punya data (self) yang terpisah satu sama lain.