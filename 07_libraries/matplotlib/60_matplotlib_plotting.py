# 1. KONSEP

# plt.plot(x, y) menggambar garis atau titik yang menghubungkan
# pasangan koordinat (x, y) yang diberikan.
#
# Format dasar:
# - plt.plot(x, y)        → garis yang menghubungkan titik-titik
# - plt.plot(x, y, "o")   → hanya titik, tanpa garis
# - plt.plot(x, y, "o-")  → titik sekaligus garis

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Plot garis dasar dengan koordinat x dan y
x = [1, 3, 5, 7]
y = [2, 6, 4, 8]

plt.plot(x, y)
plt.title("Plot Garis Dasar")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.savefig("plot_xy.png")
plt.clf()
print("plot_xy.png disimpan.")

# Hanya titik — tanpa garis penghubung
plt.plot(x, y, "o")   # "o" = lingkaran di setiap titik
plt.title("Plot Titik Saja")
plt.savefig("plot_titik.png")
plt.clf()
print("plot_titik.png disimpan.")

# Titik sekaligus garis
plt.plot(x, y, "o-")
plt.title("Plot Titik dan Garis")
plt.savefig("plot_titik_garis.png")
plt.clf()
print("plot_titik_garis.png disimpan.")

# Satu titik tunggal
plt.plot(3, 5, "o")
plt.title("Satu Titik")
plt.savefig("plot_satu_titik.png")
plt.clf()
print("plot_satu_titik.png disimpan.")

# Dua dataset dalam satu grafik
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]   # y = x²
y2 = [1, 2, 3, 4, 5]     # y = x

plt.plot(x1, y1, label="y = x²")
plt.plot(x1, y2, label="y = x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Perbandingan Dua Fungsi")
plt.legend()
plt.savefig("plot_dua_dataset.png")
plt.clf()
print("plot_dua_dataset.png disimpan.")

# Fungsi matematika — plot y = x² dalam rentang tertentu
def plot_fungsi(x_awal, x_akhir, nama_file):
    x = list(range(x_awal, x_akhir + 1))
    y = [n ** 2 for n in x]
    plt.plot(x, y)
    plt.title(f"y = x² (x dari {x_awal} sampai {x_akhir})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(nama_file)
    plt.clf()
    print(f"{nama_file} disimpan.")

plot_fungsi(0, 10, "plot_kuadrat.png")

# 3. RANGKUMAN

# - plt.plot(x, y) menggambar garis yang menghubungkan titik koordinat.
# - Tambahkan "o" untuk hanya menampilkan titik tanpa garis.
# - Tambahkan "o-" untuk titik sekaligus garis.
# - Dua plt.plot() sebelum savefig() menghasilkan dua garis dalam satu grafik.
# - Gunakan plt.legend() untuk memberi keterangan setiap garis.