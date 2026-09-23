# 1. KONSEP

# Grid adalah garis-garis bantu di latar belakang grafik.
# Membantu pembaca memperkirakan nilai pada grafik dengan lebih tepat.
#
# Fungsi yang dipakai:
# plt.grid(True)          → tampilkan grid di kedua arah
# plt.grid(axis="y")      → hanya garis horizontal
# plt.grid(axis="x")      → hanya garis vertikal
#
# Parameter tambahan:
# color     → warna garis grid
# linestyle → bentuk garis grid
# linewidth → ketebalan garis grid

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [3, 6, 9]

# Grid dasar
plt.plot(x, y)
plt.title("Grid Dasar")
plt.grid(True)
plt.savefig("plot_grid_dasar.png")
plt.clf()
print("plot_grid_dasar.png disimpan.")

# Grid horizontal saja
plt.plot(x, y)
plt.title("Grid Horizontal")
plt.grid(axis="y")
plt.savefig("plot_grid_horizontal.png")
plt.clf()
print("plot_grid_horizontal.png disimpan.")

# Grid vertikal saja
plt.plot(x, y)
plt.title("Grid Vertikal")
plt.grid(axis="x")
plt.savefig("plot_grid_vertikal.png")
plt.clf()
print("plot_grid_vertikal.png disimpan.")

# Mengubah warna dan bentuk garis grid
plt.plot(x, y)
plt.title("Grid Kustom")
plt.grid(color="green", linestyle="--", linewidth=0.5)
plt.savefig("plot_grid_kustom.png")
plt.clf()
print("plot_grid_kustom.png disimpan.")

# Membandingkan grafik tanpa grid dan dengan grid
plt.plot(x, y)
plt.title("Tanpa Grid")
plt.savefig("plot_tanpa_grid.png")
plt.clf()
print("plot_tanpa_grid.png disimpan.")

plt.plot(x, y)
plt.title("Dengan Grid")
plt.grid(True)
plt.savefig("plot_dengan_grid.png")
plt.clf()
print("plot_dengan_grid.png disimpan.")

# 3. RANGKUMAN

# - plt.grid(True) menampilkan garis bantu pada grafik.
# - axis="x" atau axis="y" membatasi grid pada satu arah saja.
# - color, linestyle, dan linewidth mengatur tampilan garis grid.
# - Grid membuat nilai pada grafik lebih mudah dibaca.