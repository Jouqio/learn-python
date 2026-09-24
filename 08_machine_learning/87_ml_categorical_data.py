# 1. KONSEP

# Data kategorikal adalah data berupa teks/label seperti "merah", "biru", "besar".
# Sebagian besar algoritma ML hanya bisa memproses angka,
# jadi data kategorikal harus diubah ke bentuk numerik terlebih dahulu.
#
# Dua metode encoding yang umum:
#
# 1. Label Encoding → setiap kategori diberi angka (merah=0, biru=1, hijau=2)
#    Masalah: model bisa salah mengasumsikan urutan (hijau > biru > merah)
#
# 2. One-Hot Encoding → setiap kategori jadi kolom baru berisi 0 atau 1
#    Lebih aman untuk kategori tanpa urutan natural

# 2. CONTOH

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

# Data contoh
df = pd.DataFrame({
    "warna" : ["merah", "biru", "hijau", "biru", "merah"],
    "ukuran": ["kecil", "besar", "sedang", "kecil", "besar"],
})

print("=== Data Asli ===")
print(df)

# One-Hot Encoding dengan pandas — paling mudah
df_onehot = pd.get_dummies(df, columns=["warna"])
print("\n=== One-Hot Encoding (pandas) ===")
print(df_onehot)

# Label Encoding — angka sederhana per kategori
le = LabelEncoder()
df["warna_encoded"] = le.fit_transform(df["warna"])

print("\n=== Label Encoding ===")
print(df[["warna", "warna_encoded"]])
print(f"Pemetaan: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Ordinal Encoding — untuk kategori yang memang punya urutan
ukuran_terurut = pd.Categorical(
    df["ukuran"],
    categories=["kecil", "sedang", "besar"],
    ordered=True
)
df["ukuran_ordinal"] = ukuran_terurut.codes
print("\n=== Ordinal Encoding (ukuran: kecil<sedang<besar) ===")
print(df[["ukuran", "ukuran_ordinal"]])

# One-Hot Encoding dengan sklearn
print("\n=== One-Hot Encoding (sklearn) ===")
ohe    = OneHotEncoder(sparse_output=False)
hasil  = ohe.fit_transform(df[["warna"]])
kolom  = ohe.get_feature_names_out(["warna"])
df_ohe = pd.DataFrame(hasil, columns=kolom, dtype=int)
print(df_ohe)

# Bahaya label encoding untuk kategori tanpa urutan
print("\n=== Bahaya Label Encoding ===")
print("Jika warna diencoding: merah=0, biru=1, hijau=2")
print("Model bisa mengira: hijau > biru > merah")
print("Padahal warna tidak punya urutan — gunakan one-hot untuk kasus ini.")

# Fungsi reusable — one-hot encode kolom tertentu
def encode_kategorikal(df, kolom):
    return pd.get_dummies(df, columns=[kolom])

df_hasil = encode_kategorikal(
    pd.DataFrame({"kota": ["Jakarta", "Bandung", "Surabaya", "Jakarta"]}),
    "kota"
)
print("\n=== Fungsi encode_kategorikal ===")
print(df_hasil)

# 3. RANGKUMAN

# - Data kategorikal harus diubah ke angka sebelum diproses model ML.
# - One-Hot Encoding membuat kolom baru per kategori — aman untuk kategori tanpa urutan.
# - Label Encoding memberi angka per kategori — hanya aman jika ada urutan natural.
# - Ordinal Encoding digunakan saat kategori memang punya urutan (kecil < sedang < besar).
# - Gunakan pd.get_dummies() untuk one-hot yang cepat, sklearn untuk pipeline ML.