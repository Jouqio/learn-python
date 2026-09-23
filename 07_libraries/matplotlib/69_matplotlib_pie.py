# 1. KONSEP

# Diagram lingkaran (pie chart) menampilkan bagian-bagian dari satu keseluruhan
# dalam bentuk irisan.
#
# Fungsi yang dipakai:
# plt.pie(nilai, labels=nama) → membuat diagram lingkaran
#
# Parameter yang sering dipakai:
# labels  → nama setiap irisan
# autopct → menampilkan persentase di setiap irisan
# explode → menggeser irisan keluar untuk menyorotinya
# colors  → daftar warna irisan
#
# Fungsi tambahan:
# plt.legend() → menampilkan keterangan irisan

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

label = ["Sewa", "Makan", "Transportasi", "Tabungan"]
nilai = [40, 25, 15, 20]

# Diagram lingkaran dasar
plt.pie(nilai, labels=label)
plt.title("Pengeluaran Bulanan")
plt.savefig("plot_pie_dasar.png")
plt.clf()
print("plot_pie_dasar.png disimpan.")

# Menampilkan persentase
plt.pie(nilai, labels=label, autopct="%1.1f%%")
plt.title("Pengeluaran dengan Persentase")
plt.savefig("plot_pie_persen.png")
plt.clf()
print("plot_pie_persen.png disimpan.")

# Menggeser satu irisan keluar
geser = [0, 0, 0, 0.1]    # irisan "Tabungan" digeser

plt.pie(nilai, labels=label, autopct="%1.1f%%", explode=geser)
plt.title("Irisan Tabungan Disorot")
plt.savefig("plot_pie_explode.png")
plt.clf()
print("plot_pie_explode.png disimpan.")

# Menambahkan legenda
plt.pie(nilai, autopct="%1.1f%%")
plt.legend(label)
plt.title("Pie dengan Legenda")
plt.savefig("plot_pie_legenda.png")
plt.clf()
print("plot_pie_legenda.png disimpan.")

# Mengubah warna irisan
warna = ["red", "orange", "yellow", "green"]

plt.pie(nilai, labels=label, autopct="%1.1f%%", colors=warna)
plt.title("Warna Kustom")
plt.savefig("plot_pie_warna.png")
plt.clf()
print("plot_pie_warna.png disimpan.")

# 3. RANGKUMAN

# - plt.pie() menampilkan proporsi bagian terhadap keseluruhan.
# - autopct="%1.1f%%" menampilkan persentase pada setiap irisan.
# - explode menggeser irisan tertentu agar menonjol.
# - colors mengatur warna irisan, plt.legend() menampilkan keterangan.
# - Pie chart paling cocok untuk sedikit kategori yang jumlahnya membentuk satu keseluruhan.