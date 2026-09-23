# 1. KONSEP

# Python punya tiga cara memformat string:
# - f-string     → cara modern, paling disarankan (Python 3.6+)
# - .format()    → cara lama, masih sering ditemui
# - % formatting → cara paling lama, hindari untuk kode baru
#
# Gunakan f-string untuk semua kode baru.

# 2. CONTOH

nama  = "Fajar"
nilai = 87.5

# Tiga cara menghasilkan output yang sama
print(f"{nama} mendapat nilai {nilai:.1f}")               # f-string
print("{} mendapat nilai {:.1f}".format(nama, nilai))     # .format()
print("%s mendapat nilai %.1f" % (nama, nilai))           # % formatting

# -- F-STRING (disarankan) --

# Desimal — mengatur jumlah angka di belakang koma
harga = 19999.9
print(f"Harga: {harga:.2f}")           # Harga: 19999.90

# Pemisah ribuan
populasi = 1500000
print(f"Populasi: {populasi:,}")       # Populasi: 1,500,000

# Padding — mengisi ruang kosong dengan angka atau spasi
nomor = 7
print(f"Nomor urut: {nomor:03d}")      # Nomor urut: 007

# Perataan teks dalam lebar tertentu
print(f"{'Kiri':<10}|{'Kanan':>10}")  # Kiri      |     Kanan
print(f"{'Tengah':^10}")               #   Tengah

# Ekspresi langsung di dalam f-string
a, b = 5, 3
print(f"{a} + {b} = {a + b}")          # 5 + 3 = 8
print(f"Nama besar: {nama.upper()}")   # Nama besar: FAJAR

# Contoh nyata: format mata uang Rupiah
def format_rupiah(jumlah):
    return f"Rp {jumlah:,.0f}".replace(",", ".")

print(format_rupiah(1234567))   # Rp 1.234.567
print(format_rupiah(50000))     # Rp 50.000

# 3. RANGKUMAN

# - Gunakan f-string: f"teks {variabel}" untuk semua kode baru.
# - :.2f → 2 angka di belakang koma.
# - :,   → pemisah ribuan otomatis.
# - :03d → padding nol di depan angka.
# - :<, :>, :^ → rata kiri, kanan, tengah dalam lebar tertentu.