# 1. KONSEP

# Subplot memungkinkan beberapa grafik ditampilkan dalam satu gambar (figure).
# Berguna untuk membandingkan beberapa grafik yang saling berhubungan.
#
# Fungsi yang dipakai:
# plt.subplots(baris, kolom) → membuat figure berisi beberapa grafik
#
# Hasilnya ada dua:
# fig  → figure (kanvas utama)
# axes → daftar area grafik, diakses dengan indeks
#
# Parameter dan fungsi tambahan:
# sharey=True       → semua grafik memakai sumbu y yang sama
# plt.tight_layout() → merapikan jarak antar grafik

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [1, 2, 3]

# Dua grafik berdampingan
fig, axes = plt.subplots(1, 2)
axes[0].plot(x, [1, 2, 3])
axes[1].plot(x, [3, 2, 1])
fig.savefig("plot_subplot_dua.png")
plt.close(fig)
print("plot_subplot_dua.png disimpan.")

# Empat grafik dalam susunan 2x2
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, [1, 2, 3])
axes[0, 1].plot(x, [3, 2, 1])
axes[1, 0].plot(x, [2, 4, 6])
axes[1, 1].plot(x, [6, 4, 2])
fig.savefig("plot_subplot_2x2.png")
plt.close(fig)
print("plot_subplot_2x2.png disimpan.")

# Judul untuk setiap grafik
fig, axes = plt.subplots(1, 2)
axes[0].plot(x, [1, 2, 3])
axes[0].set_title("Naik")
axes[1].plot(x, [3, 2, 1])
axes[1].set_title("Turun")
fig.savefig("plot_subplot_judul.png")
plt.close(fig)
print("plot_subplot_judul.png disimpan.")

# Berbagi sumbu y antar grafik
fig, axes = plt.subplots(1, 2, sharey=True)
axes[0].plot(x, [10, 20, 30])
axes[0].set_title("Data A")
axes[1].plot(x, [15, 25, 35])
axes[1].set_title("Data B")
fig.savefig("plot_subplot_sharey.png")
plt.close(fig)
print("plot_subplot_sharey.png disimpan.")

# Merapikan jarak dengan tight_layout
fig, axes = plt.subplots(1, 2)
axes[0].plot(x, [1, 2, 3])
axes[0].set_title("Grafik Pertama")
axes[1].plot(x, [3, 2, 1])
axes[1].set_title("Grafik Kedua")
fig.tight_layout()
fig.savefig("plot_subplot_rapi.png")
plt.close(fig)
print("plot_subplot_rapi.png disimpan.")

# 3. RANGKUMAN

# - plt.subplots(baris, kolom) membuat beberapa grafik dalam satu figure.
# - axes[0], axes[1] dipakai untuk grafik 1 baris; axes[baris, kolom] untuk susunan 2D.
# - set_title() memberi judul pada masing-masing grafik.
# - sharey=True membuat sumbu y sama, tight_layout() merapikan jarak antar grafik.