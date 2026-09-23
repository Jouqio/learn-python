# 1. KONSEP

# Tuple mirip dengan list, tapi nilainya TIDAK BISA diubah setelah dibuat.
# Ditulis dengan tanda kurung biasa: (item1, item2, item3)
#
# Kapan pakai tuple:
# - Data yang tidak boleh berubah (koordinat, konfigurasi, dll.)
# - Mengembalikan beberapa nilai dari sebuah fungsi
# - Unpacking — membagi isi tuple ke beberapa variabel sekaligus

# 2. CONTOH

# Membuat tuple
koordinat = (10, 20)
print(koordinat)
print(koordinat[0])  # 10
print(koordinat[1])  # 20

# Unpacking — membagi isi tuple ke variabel terpisah
x, y = koordinat
print(f"x={x}, y={y}")

# Tuple bisa berisi tipe data berbeda
profil = ("Dewi", 30, "Engineer")
nama, usia, pekerjaan = profil
print(f"{nama}, {usia} tahun, {pekerjaan}")

# Tuple tidak bisa diubah — baris ini akan error jika dijalankan:
# koordinat[0] = 99  # TypeError: 'tuple' object does not support item assignment

# Konversi tuple ↔ list jika perlu diubah sementara
sebagai_list = list(koordinat)
sebagai_list.append(30)
koordinat_baru = tuple(sebagai_list)
print(koordinat_baru)  # (10, 20, 30)

# Mengembalikan beberapa nilai dari fungsi (otomatis jadi tuple)
def statistik(data):
    return min(data), max(data), sum(data) / len(data)

nilai_min, nilai_max, rata_rata = statistik([4, 8, 15, 16, 23])
print(f"Min: {nilai_min}, Max: {nilai_max}, Rata-rata: {rata_rata}")

# Unpacking dalam for loop
daftar_siswa = [("Andi", 90), ("Budi", 85), ("Cici", 92)]
for nama, nilai in daftar_siswa:
    print(f"{nama} mendapat nilai {nilai}")

# 3. RANGKUMAN

# - Tuple seperti list tapi tidak bisa diubah setelah dibuat.
# - Gunakan unpacking untuk membagi isi tuple ke beberapa variabel.
# - Fungsi bisa mengembalikan beberapa nilai sekaligus lewat tuple.
# - Konversi ke list dulu jika perlu mengubah isinya.