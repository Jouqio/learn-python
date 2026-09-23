 # 1. KONSEP

# pyplot adalah modul utama Matplotlib yang menyediakan fungsi-fungsi
# untuk membangun grafik secara bertahap, satu perintah per baris.
#
# Cara kerjanya "berbasis state" — setiap perintah plt.xxx() menambahkan
# sesuatu ke grafik yang sedang aktif, sampai akhirnya disimpan atau ditampilkan.
#
# Fungsi pyplot yang sering dipakai:
# - plt.plot()    → menggambar garis
# - plt.xlabel()  → label sumbu x
# - plt.ylabel()  → label sumbu y
# - plt.title()   → judul grafik
# - plt.legend()  → keterangan garis
# - plt.savefig() → simpan grafik ke file

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Plot tanpa x — Matplotlib otomatis menggunakan indeks (0, 1, 2, ...)
nilai = [10, 25, 15, 30, 20]

plt.plot(nilai)
plt.xlabel("Indeks")
plt.ylabel("Nilai")
plt.title("Plot Sederhana")
plt.savefig("plot_pyplot.png")
plt.clf()
print("plot_pyplot.png disimpan.")

# Dua garis dalam satu grafik — dua plt.plot() sebelum savefig
bulan = [1, 2, 3, 4, 5]
penjualan_a = [100, 150, 120, 180, 160]
penjualan_b = [80,  110, 130, 140, 170]

plt.plot(bulan, penjualan_a, label="Produk A")
plt.plot(bulan, penjualan_b, label="Produk B")
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.title("Perbandingan Penjualan")
plt.legend()   # tampilkan keterangan label
plt.savefig("plot_dua_garis.png")
plt.clf()
print("plot_dua_garis.png disimpan.")

# Fungsi reusable — plot nilai dengan label sumbu y
def plot_cepat(nilai, label_y, nama_file):
    plt.plot(nilai)
    plt.ylabel(label_y)
    plt.xlabel("Indeks")
    plt.savefig(nama_file)
    plt.clf()
    print(f"{nama_file} disimpan.")

plot_cepat([5, 8, 6, 9, 7], "Skor", "plot_skor.png")

# 3. RANGKUMAN

# - pyplot bekerja secara bertahap — setiap perintah menambah elemen ke grafik aktif.
# - Jika x tidak diberikan, Matplotlib otomatis menggunakan indeks mulai dari 0.
# - Dua plt.plot() sebelum savefig() menghasilkan dua garis dalam satu grafik.
# - Gunakan plt.legend() untuk menampilkan keterangan setiap garis.