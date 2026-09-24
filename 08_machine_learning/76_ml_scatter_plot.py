# 1. KONSEP

# Scatter plot adalah grafik yang menampilkan hubungan antara dua variabel.
# Setiap titik mewakili satu data dengan posisi (x, y).
#
# Digunakan sebelum membuat model ML untuk melihat:
# - Apakah ada hubungan linear (titik membentuk garis lurus)?
# - Apakah ada hubungan non-linear (kurva)?
# - Apakah tidak ada hubungan sama sekali (titik acak)?

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Scatter plot dasar — jam belajar vs nilai ujian
jam_belajar = [1, 2, 3, 4, 5, 6, 7, 8]
nilai_ujian  = [50, 55, 65, 70, 72, 80, 88, 92]

plt.scatter(jam_belajar, nilai_ujian)
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")
plt.title("Hubungan Jam Belajar dan Nilai Ujian")
plt.savefig("scatter_dasar.png")
plt.clf()
print("scatter_dasar.png disimpan.")
# Hubungan terlihat LINEAR — semakin banyak belajar, nilai cenderung naik

# Dua dataset dalam satu scatter plot
jam_kelas_a  = [1, 2, 3, 4, 5, 6, 7, 8]
nilai_kelas_a = [50, 55, 65, 70, 72, 80, 88, 92]

jam_kelas_b  = [1, 2, 3, 4, 5, 6, 7, 8]
nilai_kelas_b = [45, 50, 55, 60, 65, 68, 72, 78]

plt.scatter(jam_kelas_a, nilai_kelas_a, label="Kelas A", color="steelblue")
plt.scatter(jam_kelas_b, nilai_kelas_b, label="Kelas B", color="salmon")
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")
plt.title("Perbandingan Dua Kelas")
plt.legend()
plt.savefig("scatter_dua_kelas.png")
plt.clf()
print("scatter_dua_kelas.png disimpan.")

# Warna titik berdasarkan lulus / tidak lulus
batas_lulus = 65
warna = ["green" if n >= batas_lulus else "red" for n in nilai_ujian]

plt.scatter(jam_belajar, nilai_ujian, c=warna)
plt.axhline(y=batas_lulus, color="gray", linestyle="--", label=f"Batas lulus ({batas_lulus})")
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")
plt.title("Lulus (hijau) vs Tidak Lulus (merah)")
plt.legend()
plt.savefig("scatter_lulus.png")
plt.clf()
print("scatter_lulus.png disimpan.")

# Fungsi reusable — scatter plot dua kolom data
def scatter_plot(x, y, label_x, label_y, nama_file):
    plt.scatter(x, y, color="steelblue")
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(f"{label_x} vs {label_y}")
    plt.savefig(nama_file)
    plt.clf()
    print(f"{nama_file} disimpan.")

tinggi  = [155, 160, 165, 170, 175, 180]
berat   = [50,  55,  60,  68,  72,  80]
scatter_plot(tinggi, berat, "Tinggi (cm)", "Berat (kg)", "scatter_tinggi_berat.png")

# 3. RANGKUMAN

# - plt.scatter(x, y) membuat scatter plot dari dua variabel.
# - Scatter plot adalah langkah pertama sebelum membuat model ML.
# - Hubungan linear → titik membentuk garis; non-linear → kurva; acak → tidak ada pola.
# - Gunakan parameter c untuk mewarnai titik berdasarkan kategori.
# - plt.axhline() menambahkan garis horizontal sebagai batas referensi.