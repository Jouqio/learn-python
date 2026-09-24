# 1. KONSEP

# Regresi linear mencari garis lurus terbaik yang menjelaskan
# hubungan antara variabel input (x) dan output (y).
#
# Persamaan garis: y = slope * x + intercept
# - slope     → kemiringan garis (seberapa cepat y berubah per satuan x)
# - intercept → titik potong sumbu y (nilai y saat x = 0)
#
# Nilai r (korelasi):
# - r mendekati  1 → hubungan linear positif kuat
# - r mendekati -1 → hubungan linear negatif kuat
# - r mendekati  0 → tidak ada hubungan linear

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Data jam belajar vs nilai ujian
jam_belajar = [1, 2, 3, 4, 5, 6, 7, 8]
nilai_ujian  = [50, 55, 65, 70, 72, 80, 88, 92]

# Membuat model regresi linear
slope, intercept, r, p, std_err = stats.linregress(jam_belajar, nilai_ujian)

print("=== Hasil Regresi Linear ===")
print(f"Persamaan   : y = {slope:.2f}x + {intercept:.2f}")
print(f"Slope       : {slope:.2f}  → setiap tambah 1 jam belajar, nilai naik {slope:.2f}")
print(f"Intercept   : {intercept:.2f}")
print(f"r (korelasi): {r:.3f}  → hubungan linear {'kuat' if abs(r) > 0.8 else 'lemah'}")

# Prediksi nilai untuk jam belajar yang belum ada di data
def prediksi_nilai(jam, jam_data, nilai_data):
    slope, intercept, r, _, _ = stats.linregress(jam_data, nilai_data)
    hasil = slope * jam + intercept
    return round(hasil, 1)

print(f"\nPrediksi nilai untuk 6.5 jam : {prediksi_nilai(6.5, jam_belajar, nilai_ujian)}")
print(f"Prediksi nilai untuk 10 jam  : {prediksi_nilai(10, jam_belajar, nilai_ujian)}")

# Visualisasi titik data + garis regresi
x_garis = np.linspace(min(jam_belajar), max(jam_belajar), 100)
y_garis = slope * x_garis + intercept

plt.scatter(jam_belajar, nilai_ujian, color="steelblue", label="Data asli")
plt.plot(x_garis, y_garis, color="salmon", label=f"y = {slope:.2f}x + {intercept:.2f}")
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai Ujian")
plt.title("Regresi Linear: Jam Belajar vs Nilai Ujian")
plt.legend()
plt.savefig("plot_regresi_linear.png")
plt.clf()
print("\nplot_regresi_linear.png disimpan.")

# 3. RANGKUMAN

# - Regresi linear mencari garis terbaik: y = slope * x + intercept.
# - slope menunjukkan seberapa besar y berubah untuk setiap kenaikan x.
# - Nilai r mendekati 1 atau -1 → hubungan linear kuat; mendekati 0 → lemah.
# - Gunakan stats.linregress() dari scipy untuk menghitung regresi.
# - Model bisa digunakan untuk memprediksi nilai y dari x yang baru.