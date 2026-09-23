# 1. KONSEP

# Gaya garis (line style) mengatur tampilan garis pada grafik.
# Ada tiga hal yang bisa diubah: bentuk garis, warna, dan ketebalan.
#
# Parameter yang sering dipakai:
# linestyle → bentuk garis
# color     → warna garis
# linewidth → ketebalan garis
#
# Jenis linestyle yang sering dipakai:
# "solid"   atau "-"   → garis biasa (bawaan)
# "dashed"  atau "--"  → garis putus-putus
# "dotted"  atau ":"   → garis titik-titik
# "dashdot" atau "-."  → garis putus-titik

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

y = [1, 2, 3, 4]

# Garis putus-putus
plt.plot(y, linestyle="dashed")
plt.title("Garis Putus-putus")
plt.savefig("plot_line_dashed.png")
plt.clf()
print("plot_line_dashed.png disimpan.")

# Mengubah warna garis
plt.plot(y, color="red")
plt.title("Garis Merah")
plt.savefig("plot_line_warna.png")
plt.clf()
print("plot_line_warna.png disimpan.")

# Mengubah ketebalan garis
plt.plot(y, linewidth=5)
plt.title("Garis Tebal")
plt.savefig("plot_line_tebal.png")
plt.clf()
print("plot_line_tebal.png disimpan.")

# Menggabungkan linestyle, color, dan linewidth
plt.plot(y, linestyle="dashed", color="red", linewidth=2)
plt.title("Gaya Garis Gabungan")
plt.savefig("plot_line_gabungan.png")
plt.clf()
print("plot_line_gabungan.png disimpan.")

# Dua garis dengan gaya berbeda dalam satu grafik
nilai_asli = [3, 5, 2, 7]
nilai_prediksi = [4, 4, 3, 6]

plt.plot(nilai_asli, linestyle="solid", color="blue", label="Asli")
plt.plot(nilai_prediksi, linestyle="dashed", color="red", label="Prediksi")
plt.title("Perbandingan Dua Garis")
plt.legend()
plt.savefig("plot_line_perbandingan.png")
plt.clf()
print("plot_line_perbandingan.png disimpan.")

# 3. RANGKUMAN

# - linestyle mengatur bentuk garis: "solid", "dashed", "dotted", "dashdot".
# - color mengatur warna garis.
# - linewidth mengatur ketebalan garis.
# - Gaya garis yang berbeda membantu membedakan beberapa garis dalam satu grafik.