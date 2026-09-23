# 1. KONSEP

# Scatter plot menampilkan titik-titik (x, y) tanpa garis penghubung.
# Cocok untuk melihat hubungan (korelasi) antara dua data angka.
#
# Fungsi yang dipakai:
# plt.scatter(x, y) → membuat scatter plot
#
# Parameter yang sering dipakai:
# s     → ukuran titik
# c     → warna titik (satu warna, atau daftar angka untuk mewarnai per titik)
# color → warna satu kelompok titik
# label → nama kelompok titik (untuk legenda)

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 2, 17, 2, 9]
y = [99, 86, 87, 88, 100, 86, 103, 87]

# Scatter plot dasar
plt.scatter(x, y)
plt.title("Scatter Plot Dasar")
plt.savefig("plot_scatter_dasar.png")
plt.clf()
print("plot_scatter_dasar.png disimpan.")

# Mewarnai titik berdasarkan variabel ketiga
nilai_warna = [10, 20, 30, 40, 50, 60, 70, 80]

plt.scatter(x, y, c=nilai_warna)
plt.title("Titik Berwarna")
plt.colorbar()
plt.savefig("plot_scatter_warna.png")
plt.clf()
print("plot_scatter_warna.png disimpan.")

# Mengubah ukuran titik
plt.scatter(x, y, s=100)
plt.title("Ukuran Titik Besar")
plt.savefig("plot_scatter_ukuran.png")
plt.clf()
print("plot_scatter_ukuran.png disimpan.")

# Menambahkan judul dan label sumbu
plt.scatter(x, y)
plt.title("Umur dan Kecepatan Mobil")
plt.xlabel("Umur Mobil (tahun)")
plt.ylabel("Kecepatan (km/jam)")
plt.savefig("plot_scatter_label.png")
plt.clf()
print("plot_scatter_label.png disimpan.")

# Dua kelompok data dengan warna berbeda
x_a = [5, 7, 8, 7, 2]
y_a = [99, 86, 87, 88, 100]
x_b = [17, 2, 9, 4, 11]
y_b = [86, 103, 87, 94, 78]

plt.scatter(x_a, y_a, color="blue", label="Kelompok A")
plt.scatter(x_b, y_b, color="red", label="Kelompok B")
plt.title("Dua Kelompok Data")
plt.legend()
plt.savefig("plot_scatter_dua_kelompok.png")
plt.clf()
print("plot_scatter_dua_kelompok.png disimpan.")

# 3. RANGKUMAN

# - plt.scatter(x, y) menampilkan titik tanpa garis penghubung.
# - s mengatur ukuran titik, c mengatur warna titik.
# - c bisa berupa daftar angka, dan plt.colorbar() menampilkan skala warnanya.
# - Scatter plot cocok untuk melihat hubungan antara dua variabel angka.