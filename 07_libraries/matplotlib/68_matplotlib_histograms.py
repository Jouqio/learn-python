# 1. KONSEP

# Histogram menampilkan sebaran (distribusi) data angka.
# Data dikelompokkan ke dalam rentang nilai yang disebut bin,
# lalu tinggi batang menunjukkan berapa banyak data di setiap bin.
#
# Fungsi yang dipakai:
# plt.hist(data, bins=jumlah_bin) → membuat histogram
# plt.axvline(x)                  → menggambar garis vertikal di nilai x
#
# Parameter yang sering dipakai:
# bins  → jumlah kelompok (bin)
# alpha → transparansi (0 = transparan, 1 = solid)
# label → nama data (untuk legenda)

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Membuat 200 data acak dengan rata-rata 70
data = np.random.default_rng(1).normal(loc=70, scale=10, size=200)

# Histogram dasar
plt.hist(data, bins=15)
plt.title("Histogram Dasar")
plt.savefig("plot_hist_dasar.png")
plt.clf()
print("plot_hist_dasar.png disimpan.")

# Membandingkan jumlah bin
plt.hist(data, bins=5)
plt.title("Bin Sedikit (5)")
plt.savefig("plot_hist_bin_sedikit.png")
plt.clf()
print("plot_hist_bin_sedikit.png disimpan.")

plt.hist(data, bins=40)
plt.title("Bin Banyak (40)")
plt.savefig("plot_hist_bin_banyak.png")
plt.clf()
print("plot_hist_bin_banyak.png disimpan.")

# Menambahkan label sumbu
plt.hist(data, bins=15)
plt.title("Sebaran Nilai Ujian")
plt.xlabel("Nilai")
plt.ylabel("Jumlah Siswa")
plt.savefig("plot_hist_label.png")
plt.clf()
print("plot_hist_label.png disimpan.")

# Dua histogram dengan transparansi
kelas_a = np.random.default_rng(1).normal(loc=70, scale=10, size=200)
kelas_b = np.random.default_rng(2).normal(loc=80, scale=8, size=200)

plt.hist(kelas_a, bins=15, alpha=0.5, label="Kelas A")
plt.hist(kelas_b, bins=15, alpha=0.5, label="Kelas B")
plt.title("Perbandingan Dua Kelas")
plt.legend()
plt.savefig("plot_hist_dua_data.png")
plt.clf()
print("plot_hist_dua_data.png disimpan.")

# Garis vertikal untuk rata-rata
rata_rata = np.mean(data)

plt.hist(data, bins=15)
plt.axvline(rata_rata, color="red", linestyle="--", label="Rata-rata")
plt.title("Histogram dengan Garis Rata-rata")
plt.legend()
plt.savefig("plot_hist_rata_rata.png")
plt.clf()
print("plot_hist_rata_rata.png disimpan.")

# 3. RANGKUMAN

# - plt.hist() menampilkan sebaran data dengan mengelompokkannya ke dalam bin.
# - bins mengatur jumlah kelompok: terlalu sedikit atau terlalu banyak bisa menyulitkan pembacaan.
# - alpha membuat transparan sehingga dua histogram bisa ditumpuk.
# - plt.axvline() menambahkan garis vertikal, misalnya untuk menandai rata-rata.