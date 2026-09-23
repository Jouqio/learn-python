# 1. KONSEP

# Marker adalah simbol yang ditampilkan di setiap titik data pada grafik.
# Membantu membedakan titik data, terutama pada data yang jarang.
#
# Marker yang sering dipakai:
# "o"  → lingkaran       "s"  → kotak
# "^"  → segitiga atas   "v"  → segitiga bawah
# "*"  → bintang         "D"  → berlian
# "+"  → plus            "x"  → silang
#
# Format singkat: "warna + garis + marker"
# Contoh: "r--o" → merah, garis putus-putus, marker lingkaran

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 7, 4]

# Marker dasar — lingkaran
plt.plot(x, y, marker="o")
plt.title("Marker Lingkaran")
plt.savefig("plot_marker_o.png")
plt.clf()
print("plot_marker_o.png disimpan.")

# Berbagai jenis marker
marker_list = [("o", "Lingkaran"), ("s", "Kotak"), ("^", "Segitiga"), ("*", "Bintang")]

for simbol, nama in marker_list:
    plt.plot(x, y, marker=simbol, label=nama)

plt.title("Berbagai Jenis Marker")
plt.legend()
plt.savefig("plot_marker_berbagai.png")
plt.clf()
print("plot_marker_berbagai.png disimpan.")

# Format string singkat — warna + garis + marker
plt.plot(x, y, "r--o")    # merah, garis putus-putus, marker lingkaran
plt.title("Format Singkat: r--o")
plt.savefig("plot_marker_format.png")
plt.clf()
print("plot_marker_format.png disimpan.")

# Mengubah ukuran dan warna marker
plt.plot(x, y,
    marker="o",
    markersize=12,             # ukuran marker
    markerfacecolor="yellow",  # warna dalam marker
    markeredgecolor="blue",    # warna tepi marker
    color="gray"               # warna garis
)
plt.title("Marker Kustom")
plt.savefig("plot_marker_kustom.png")
plt.clf()
print("plot_marker_kustom.png disimpan.")

# Tiga marker berbeda dalam subplot berdampingan
fig, axes = plt.subplots(1, 3, figsize=(10, 3))

marker_subplot = [("o", "Lingkaran"), ("s", "Kotak"), ("*", "Bintang")]

for ax, (simbol, nama) in zip(axes, marker_subplot):
    ax.plot(x, y, marker=simbol)
    ax.set_title(nama)

plt.tight_layout()
plt.savefig("plot_marker_subplot.png")
plt.clf()
print("plot_marker_subplot.png disimpan.")

# 3. RANGKUMAN

# - Gunakan marker="o" (atau simbol lain) untuk menandai titik data.
# - Format singkat "r--o" → merah, garis putus-putus, marker lingkaran.
# - markersize mengatur ukuran marker.
# - markerfacecolor dan markeredgecolor mengatur warna marker.