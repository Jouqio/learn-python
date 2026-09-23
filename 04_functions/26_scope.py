# 1. KONSEP

# Scope menentukan di mana sebuah variabel bisa diakses.
#
# Jenis scope di Python:
# - Local  → variabel di dalam fungsi, hanya bisa diakses di situ
# - Global → variabel di luar fungsi, bisa diakses di mana saja
#
# Kata kunci tambahan:
# - global   → mengizinkan fungsi mengubah variabel global
# - nonlocal → mengizinkan fungsi dalam mengubah variabel fungsi luarnya

# 2. CONTOH

# Scope lokal — variabel di dalam fungsi tidak memengaruhi luar
def sapa():
    pesan = "Halo dari dalam fungsi"  # variabel lokal
    print(pesan)

sapa()
# print(pesan)  # ini akan error — pesan tidak ada di luar fungsi

# Variabel global — bisa dibaca dari dalam fungsi
nama = "Syauqi"  # variabel global

def cetak_nama():
    print(nama)  # membaca variabel global — boleh

cetak_nama()  # Syauqi

# global — mengizinkan fungsi mengubah variabel global
penghitung = 0

def tambah():
    global penghitung   # deklarasi bahwa ini variabel global
    penghitung += 1

tambah()
tambah()
print(penghitung)       # 2

# Variabel lokal vs global dengan nama sama
nilai = 100             # variabel global

def ubah_nilai():
    nilai = 999         # ini variabel LOKAL, tidak memengaruhi yang global
    print(f"Di dalam fungsi: {nilai}")

ubah_nilai()
print(f"Di luar fungsi: {nilai}")   # tetap 100

# nonlocal — mengubah variabel di fungsi luar (bukan global)
def fungsi_luar():
    angka = 10

    def fungsi_dalam():
        nonlocal angka  # mengacu ke variabel fungsi_luar
        angka += 5

    fungsi_dalam()
    print(angka)        # 15

fungsi_luar()

# Closure — alternatif global yang lebih aman
# Menyimpan state privat tanpa variabel global
def buat_penghitung():
    jumlah = 0          # state privat, tidak bisa diakses dari luar

    def tambah():
        nonlocal jumlah
        jumlah += 1
        return jumlah

    def kurang():
        nonlocal jumlah
        jumlah -= 1
        return jumlah

    def ambil():
        return jumlah

    return tambah, kurang, ambil

tambah, kurang, ambil = buat_penghitung()
print(tambah())  # 1
print(tambah())  # 2
print(kurang())  # 1
print(ambil())   # 1

# 3. RANGKUMAN

# - Variabel lokal hanya hidup di dalam fungsi tempat ia dibuat.
# - Variabel global bisa dibaca dari mana saja, tapi ubah dengan hati-hati.
# - Gunakan global untuk mengubah variabel global dari dalam fungsi.
# - Gunakan nonlocal untuk mengubah variabel fungsi di satu level di atasnya.
# - Hindari terlalu banyak variabel global — gunakan parameter atau closure.