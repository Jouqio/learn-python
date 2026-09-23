# 1. KONSEP

# Pandas adalah library untuk mengolah data berbentuk tabel (seperti Excel).
# Ada dua struktur data utama:
# Series    → satu kolom data dengan indeks
# DataFrame → tabel berisi baris dan kolom
#
# Instalasi: pip install pandas matplotlib
#
# Hal-hal yang dibahas:
# pd.Series()          → membuat Series
# pd.DataFrame()       → membuat tabel dari dictionary
# to_csv(), read_csv() → menyimpan dan membaca file CSV
# describe(), head()   → melihat ringkasan dan isi awal data
# dropna(), fillna()   → menangani data kosong
# to_numeric()         → memperbaiki format data
# duplicated()         → mencari data ganda
# drop_duplicates()    → menghapus data ganda
# corr()               → menghitung korelasi antar kolom
# plot()               → membuat grafik dari tabel

# 2. CONTOH

import pandas as pd
import matplotlib
matplotlib.use("Agg")

# Series — satu kolom data dengan indeks
nilai = pd.Series([80, 90, 75], index=["Ani", "Budi", "Citra"])
print("Series:")
print(nilai)

# DataFrame — tabel dari dictionary
data = {
    "nama": ["Ani", "Budi", "Citra", "Dedi"],
    "nilai": [80, 90, 75, None],
    "kehadiran": [95, 88, 92, 70],
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Menyimpan dan membaca file CSV
df.to_csv("siswa.csv", index=False)
hasil_baca = pd.read_csv("siswa.csv")
print("\nDibaca dari CSV:")
print(hasil_baca)

# Menganalisis data
print("\nRingkasan statistik:")
print(df.describe())

print("\n2 baris pertama:")
print(df.head(2))

# Membersihkan data kosong
tanpa_kosong = df.dropna()    # hapus baris yang kosong
print("\nSetelah dropna():")
print(tanpa_kosong)

isi_nol = df.fillna(0)        # isi data kosong dengan 0
print("\nSetelah fillna(0):")
print(isi_nol)

# Memperbaiki format data (teks menjadi angka)
df["kehadiran"] = pd.to_numeric(df["kehadiran"], errors="coerce")

# Mencari dan menghapus data ganda
df_ganda = pd.concat([df, df.iloc[[0]]], ignore_index=True)    # tambah baris duplikat
print("\nAda data ganda:", df_ganda.duplicated().any())

df_bersih = df_ganda.drop_duplicates()
print("Jumlah baris setelah drop_duplicates:", len(df_bersih))

# Korelasi antar kolom
df_lengkap = df.dropna()
print("\nMatriks korelasi:")
print(df_lengkap[["nilai", "kehadiran"]].corr())

# Membuat grafik dari DataFrame
grafik = df_lengkap.plot(x="nama", y="nilai", kind="bar", legend=False)
grafik.figure.savefig("plot_pandas_nilai.png")
print("\nplot_pandas_nilai.png disimpan.")

# 3. RANGKUMAN

# - Series adalah satu kolom data, DataFrame adalah tabel dengan banyak kolom.
# - to_csv() menyimpan tabel ke file, read_csv() membacanya kembali.
# - describe() memberi ringkasan statistik, head() menampilkan baris awal.
# - dropna() menghapus baris kosong, fillna() mengisinya dengan nilai lain.
# - to_numeric() mengubah teks menjadi angka.
# - duplicated() mencari data ganda, drop_duplicates() menghapusnya.
# - corr() menghitung hubungan antar kolom, plot() membuat grafik dari tabel.