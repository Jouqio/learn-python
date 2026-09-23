# 1. KONSEP

# Judul dan label membuat grafik bisa dipahami tanpa penjelasan tambahan.
#
# Fungsi yang sering dipakai:
# plt.title()   → judul grafik
# plt.xlabel()  → label sumbu x (horizontal)
# plt.ylabel()  → label sumbu y (vertikal)
# plt.legend()  → keterangan garis (butuh parameter label di plt.plot)
#
# Parameter tambahan:
# fontsize → ukuran huruf
# pad      → jarak judul dari grafik

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

bulan = [1, 2, 3]
pertumbuhan = [10, 20, 25]

# Judul grafik
plt.plot(bulan, pertumbuhan)
plt.title("Pertumbuhan Bulanan")
plt.savefig("plot_label_judul.png")
plt.clf()
print("plot_label_judul.png disimpan.")

# Label sumbu x dan y
plt.plot(bulan, pertumbuhan)
plt.title("Pertumbuhan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Pertumbuhan (%)")
plt.savefig("plot_label_sumbu.png")
plt.clf()
print("plot_label_sumbu.png disimpan.")

# Mengubah ukuran huruf judul
plt.plot(bulan, pertumbuhan)
plt.title("Pertumbuhan Bulanan", fontsize=20)
plt.xlabel("Bulan")
plt.ylabel("Pertumbuhan (%)")
plt.savefig("plot_label_fontsize.png")
plt.clf()
print("plot_label_fontsize.png disimpan.")

# Menambahkan legenda
plt.plot(bulan, pertumbuhan, label="Pertumbuhan Toko A")
plt.title("Pertumbuhan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Pertumbuhan (%)")
plt.legend()
plt.savefig("plot_label_legenda.png")
plt.clf()
print("plot_label_legenda.png disimpan.")

# Mengatur jarak judul dengan pad
plt.plot(bulan, pertumbuhan)
plt.title("Pertumbuhan Bulanan", pad=20)
plt.xlabel("Bulan")
plt.ylabel("Pertumbuhan (%)")
plt.savefig("plot_label_pad.png")
plt.clf()
print("plot_label_pad.png disimpan.")

# 3. RANGKUMAN

# - plt.title() memberi judul, plt.xlabel() dan plt.ylabel() memberi label sumbu.
# - fontsize mengatur ukuran huruf.
# - plt.legend() menampilkan keterangan garis (isi lewat parameter label).
# - pad mengatur jarak antara judul dan grafik.