# 1. KONSEP

# Alur kerja dasar Matplotlib:
# 1. Import pyplot
# 2. Siapkan data (x dan y)
# 3. Buat plot
# 4. Tambahkan label/judul (opsional)
# 5. Simpan atau tampilkan
#
# plt.show()     → tampilkan di layar (saat menggunakan Jupyter/IDE)
# plt.savefig()  → simpan sebagai file gambar
# plt.clf()      → bersihkan figure agar plot berikutnya tidak menumpuk

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Plot dasar — x dan y sebagai list
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]   # y = x²

plt.plot(x, y)
plt.title("Grafik y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot_mulai.png")
plt.clf()   # bersihkan sebelum plot berikutnya
print("plot_mulai.png disimpan.")

# Membuat dan menyimpan beberapa plot dalam satu script
dataset = [
    ([1, 2, 3, 4], [10, 20, 15, 25], "Penjualan",  "plot_1.png"),
    ([1, 2, 3, 4], [5,  8,  6,  9],  "Pengunjung", "plot_2.png"),
    ([1, 2, 3, 4], [30, 25, 35, 28], "Suhu",       "plot_3.png"),
]

for x, y, judul, nama_file in dataset:
    plt.plot(x, y)
    plt.title(judul)
    plt.savefig(nama_file)
    plt.clf()   # wajib dibersihkan setelah setiap simpan
    print(f"{nama_file} disimpan.")

# 3. RANGKUMAN

# - Alur kerja: import → siapkan data → plot → beri label → simpan.
# - plt.savefig() menyimpan gambar, plt.show() menampilkan di layar.
# - Selalu panggil plt.clf() atau plt.close() setelah menyimpan
#   agar plot berikutnya tidak menumpuk di atas plot sebelumnya.