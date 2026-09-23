# 1. KONSEP

# Matplotlib adalah library visualisasi data paling populer di Python.
# Digunakan untuk membuat grafik, chart, dan plot dari data.
#
# Modul utama yang dipakai: matplotlib.pyplot (diimport sebagai plt)
# Dua cara menampilkan hasil:
# - plt.show()     → tampilkan di layar (interaktif)
# - plt.savefig()  → simpan sebagai file gambar (PNG, JPG, PDF)

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")   # mode tanpa tampilan layar — untuk menyimpan file
import matplotlib.pyplot as plt

# Cek versi matplotlib
print(f"Versi matplotlib: {matplotlib.__version__}")

# Plot sederhana
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("Plot Pertamaku")
plt.savefig("plot_intro.png")
plt.close()   # tutup figure agar tidak menumpuk saat membuat banyak plot
print("Plot disimpan sebagai plot_intro.png")

# Membuat dua plot terpisah dalam satu script
# Plot 1 — data penjualan
plt.plot([1, 2, 3, 4], [100, 150, 120, 200])
plt.title("Data Penjualan")
plt.xlabel("Bulan")
plt.ylabel("Jumlah")
plt.savefig("plot_penjualan.png")
plt.close()
print("plot_penjualan.png disimpan.")

# Plot 2 — data suhu
plt.plot([1, 2, 3, 4], [28, 30, 27, 31])
plt.title("Data Suhu Harian")
plt.xlabel("Hari")
plt.ylabel("Suhu (°C)")
plt.savefig("plot_suhu.png")
plt.close()
print("plot_suhu.png disimpan.")

# Fungsi reusable — membuat dan menyimpan line plot
def simpan_line_plot(x, y, judul, nama_file):
    plt.plot(x, y)
    plt.title(judul)
    plt.savefig(nama_file)
    plt.close()
    print(f"{nama_file} disimpan.")

simpan_line_plot([1, 2, 3], [5, 8, 6], "Contoh Plot", "plot_custom.png")

# 3. RANGKUMAN

# - Matplotlib adalah library visualisasi data utama di Python.
# - Import dengan: import matplotlib.pyplot as plt
# - plt.plot() untuk membuat grafik garis sederhana.
# - plt.title(), plt.xlabel(), plt.ylabel() untuk memberi label.
# - plt.savefig() untuk menyimpan ke file, plt.close() setelah selesai.