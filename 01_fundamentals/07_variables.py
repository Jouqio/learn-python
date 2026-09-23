# 1. KONSEP

# Variabel adalah nama yang menyimpan sebuah nilai.
# Python menentukan tipe data secara otomatis dari nilai yang diberikan
# (tidak perlu ditulis manual seperti di bahasa lain).
#
# Aturan penamaan variabel:
# - Gunakan huruf kecil dan garis bawah: nama_siswa
# - Tidak boleh diawali angka: 1nama ✗
# - Konstanta ditulis HURUF_BESAR: TARIF_PAJAK

# 2. CONTOH

# Membuat variabel
nama_siswa = "Syauqi"
usia = 21
aktif = True

print(nama_siswa, usia, aktif)

# Mengecek tipe data variabel
print(type(nama_siswa))  # <class 'str'>
print(type(usia))        # <class 'int'>
print(type(aktif))       # <class 'bool'>

# Variabel bisa diubah nilainya kapan saja
usia = 22
print(usia)  # 22

# Multiple assignment — memberi nilai ke beberapa variabel sekaligus
x, y, z = 1, 2, 3
print(x, y, z)

# Menukar nilai dua variabel (tanpa variabel ketiga)
a = "pertama"
b = "kedua"
a, b = b, a
print(a, b)  # kedua pertama

# Konstanta — nilai yang tidak boleh diubah (konvensi: HURUF_BESAR)
TARIF_PAJAK = 0.11

# 3. RANGKUMAN

# - Variabel menyimpan nilai dan dibuat otomatis saat pertama kali diisi.
# - Python menentukan tipe data sendiri — tidak perlu dideklarasikan.
# - Nama variabel yang jelas membuat kode lebih mudah dibaca.