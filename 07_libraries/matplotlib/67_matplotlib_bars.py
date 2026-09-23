# 1. KONSEP

# Diagram batang membandingkan jumlah atau nilai antar kategori.
#
# Fungsi yang dipakai:
# plt.bar(kategori, nilai)   → batang vertikal
# plt.barh(kategori, nilai)  → batang horizontal
#
# Parameter yang sering dipakai:
# color → warna batang
# width → lebar batang (untuk plt.bar)
#
# Fungsi tambahan:
# plt.text(x, y, teks) → menulis teks di posisi tertentu pada grafik

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

kategori = ["A", "B", "C"]
nilai = [3, 7, 5]

# Diagram batang vertikal
plt.bar(kategori, nilai)
plt.title("Batang Vertikal")
plt.savefig("plot_bar_vertikal.png")
plt.clf()
print("plot_bar_vertikal.png disimpan.")

# Diagram batang horizontal
plt.barh(kategori, nilai)
plt.title("Batang Horizontal")
plt.savefig("plot_bar_horizontal.png")
plt.clf()
print("plot_bar_horizontal.png disimpan.")

# Mengubah warna dan lebar batang
plt.bar(kategori, nilai, color="green", width=0.4)
plt.title("Warna dan Lebar Batang")
plt.savefig("plot_bar_kustom.png")
plt.clf()
print("plot_bar_kustom.png disimpan.")

# Menampilkan nilai di atas setiap batang
plt.bar(kategori, nilai)
for i in range(len(kategori)):
    plt.text(i, nilai[i] + 0.1, str(nilai[i]), ha="center")
plt.title("Nilai di Atas Batang")
plt.savefig("plot_bar_nilai.png")
plt.clf()
print("plot_bar_nilai.png disimpan.")

# Diagram batang berkelompok (dua data dibandingkan)
posisi = [0, 1, 2]
posisi_kanan = [0.4, 1.4, 2.4]
nilai_2024 = [3, 7, 5]
nilai_2025 = [4, 6, 8]

plt.bar(posisi, nilai_2024, width=0.4, label="2024")
plt.bar(posisi_kanan, nilai_2025, width=0.4, label="2025")
plt.xticks([0.2, 1.2, 2.2], kategori)
plt.title("Batang Berkelompok")
plt.legend()
plt.savefig("plot_bar_kelompok.png")
plt.clf()
print("plot_bar_kelompok.png disimpan.")

# 3. RANGKUMAN

# - plt.bar() membuat batang vertikal, plt.barh() membuat batang horizontal.
# - color mengatur warna, width mengatur lebar batang.
# - plt.text() dipakai untuk menampilkan nilai di atas batang.
# - Batang berkelompok dibuat dengan menggeser posisi batang kedua.