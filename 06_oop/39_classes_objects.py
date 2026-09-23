# 1. KONSEP

# Class adalah blueprint (cetakan); objek adalah hasil nyata dari cetakan itu.
# Setiap objek punya data (atribut) sendiri meski dibuat dari class yang sama.

# 2. CONTOH

# Membuat class
class Mobil:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        return f"{self.merek} ({self.tahun})"

# Membuat beberapa objek dari class yang sama
mobil1 = Mobil("Toyota", 2020)
mobil2 = Mobil("Honda", 2022)

print(mobil1.info())   # Toyota (2020)
print(mobil2.info())   # Honda (2022)

# Mengakses atribut langsung
print(mobil1.merek)    # Toyota
print(mobil2.tahun)    # 2022

# Mengecek tipe objek
print(type(mobil1))                    # <class '__main__.Mobil'>
print(isinstance(mobil1, Mobil))       # True

# Membuat list objek dan melakukan iterasi
daftar_mobil = [
    Mobil("Toyota", 2020),
    Mobil("Honda", 2022),
    Mobil("Suzuki", 2019),
]

for mobil in daftar_mobil:
    print(mobil.info())

# Contoh nyata: class Siswa dengan daftar nilai
class Siswa:
    def __init__(self, nama, nilai):
        self.nama  = nama
        self.nilai = nilai   # list angka

    def rata_rata(self):
        return sum(self.nilai) / len(self.nilai)

    def info(self):
        return f"{self.nama} — rata-rata: {self.rata_rata():.1f}"

    def lebih_tinggi_dari(self, siswa_lain):
        return self.rata_rata() > siswa_lain.rata_rata()

siswa1 = Siswa("Andi", [80, 90, 85])
siswa2 = Siswa("Budi", [70, 75, 72])

print(siswa1.info())  # Andi — rata-rata: 85.0
print(siswa2.info())  # Budi — rata-rata: 72.3

# Membandingkan dua objek
if siswa1.lebih_tinggi_dari(siswa2):
    print(f"{siswa1.nama} punya nilai lebih tinggi.")
else:
    print(f"{siswa2.nama} punya nilai lebih tinggi.")

# 3. RANGKUMAN

# - Class mendefinisikan struktur; objek menyimpan data sesungguhnya.
# - Setiap objek punya atributnya sendiri meski dari class yang sama.
# - Gunakan type() untuk melihat class sebuah objek.
# - Gunakan isinstance() untuk mengecek apakah objek berasal dari class tertentu.