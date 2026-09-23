# 1. KONSEP

# Fungsi adalah blok kode yang diberi nama dan bisa dipanggil berkali-kali.
# Digunakan untuk mengelompokkan kode yang sering dipakai agar tidak perlu
# ditulis ulang.
#
# Anatomi fungsi:
# def nama_fungsi(parameter):
#     kode di sini
#     return hasil

# 2. CONTOH

# Fungsi dasar — tanpa parameter, tanpa return
def sapa():
    print("Halo, selamat datang!")

sapa()  # memanggil fungsi

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Andi")

# Fungsi dengan nilai return
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)  # 8

# Parameter default — nilai dipakai jika argumen tidak diberikan
def hitung_total(harga, jumlah, diskon=0.0):
    subtotal = harga * jumlah
    return subtotal - (subtotal * diskon)

print(hitung_total(50000, 3))              # tanpa diskon → 150000
print(hitung_total(50000, 3, diskon=0.1)) # dengan diskon 10% → 135000.0

# Keyword argument — menyebut nama parameter saat memanggil fungsi
def perkenalan(nama, kota, usia):
    print(f"{nama}, {usia} tahun, dari {kota}")

perkenalan(nama="Budi", usia=22, kota="Bontang")  # urutan bebas

# *args — menerima banyak argumen sekaligus
def jumlahkan(*angka):
    return sum(angka)

print(jumlahkan(1, 2, 3))        # 6
print(jumlahkan(10, 20, 30, 40)) # 100

# **kwargs — menerima banyak argumen berbentuk kunci-nilai
def tampilkan_info(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

tampilkan_info(nama="Citra", jurusan="Informatika", angkatan=2022)

# 3. RANGKUMAN

# - Fungsi dibuat dengan def, dipanggil dengan nama_fungsi().
# - Parameter adalah variabel input fungsi.
# - return mengembalikan nilai dari fungsi.
# - Parameter default digunakan jika argumen tidak diberikan.
# - *args untuk banyak argumen, **kwargs untuk argumen kunci-nilai.