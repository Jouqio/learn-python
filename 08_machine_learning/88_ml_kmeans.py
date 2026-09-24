# 1. KONSEP

# K-Means adalah algoritma pengelompokan (clustering) yang membagi data
# menjadi k kelompok berdasarkan kedekatan titik ke pusat cluster.
#
# Cara kerjanya:
# 1. Pilih k pusat cluster secara acak
# 2. Setiap titik data dikelompokkan ke pusat terdekat
# 3. Pusat cluster diperbarui ke rata-rata anggotanya
# 4. Ulangi langkah 2-3 sampai tidak ada perubahan
#
# Parameter penting:
# - n_clusters → jumlah cluster yang diinginkan (harus ditentukan di awal)
# - n_init     → berapa kali algoritma diulang dengan inisialisasi berbeda
# - inertia_   → total jarak semua titik ke pusat clusternya (semakin kecil semakin baik)

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data titik 2D
titik = np.array([
    [4, 21], [5, 19], [10, 24],
    [4, 17], [3, 16], [11, 25], [14, 24]
])

# K-Means dengan 2 cluster
model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(titik)

print("=== K-Means: 2 Cluster ===")
print(f"Label cluster : {model.labels_}")
print(f"Pusat cluster :\n{model.cluster_centers_.round(2)}")
print(f"Inertia       : {model.inertia_:.2f}")

# Detail per titik
for i, (xy, label) in enumerate(zip(titik, model.labels_)):
    print(f"  Titik {i+1} {xy} → Cluster {label}")

# Perbandingan k=2 vs k=3
print("\n=== Perbandingan Jumlah Cluster ===")
for k in [2, 3]:
    m = KMeans(n_clusters=k, random_state=42, n_init=10)
    m.fit(titik)
    print(f"k={k} → label: {m.labels_}, inertia: {m.inertia_:.2f}")

# Prediksi cluster untuk titik baru
titik_baru = np.array([[6, 20]])
prediksi   = model.predict(titik_baru)
print(f"\nTitik baru {titik_baru[0]} → Cluster {prediksi[0]}")

# Metode Elbow — mencari nilai k yang optimal
def cari_k_terbaik(data, rentang_k):
    inertia_per_k = {}
    for k in rentang_k:
        m = KMeans(n_clusters=k, random_state=42, n_init=10)
        m.fit(data)
        inertia_per_k[k] = round(m.inertia_, 2)
    return inertia_per_k

hasil_elbow = cari_k_terbaik(titik, range(1, 6))
print("\n=== Metode Elbow (Inertia per k) ===")
for k, inertia in hasil_elbow.items():
    print(f"k={k} → inertia: {inertia}")
print("Pilih k di mana penurunan inertia mulai melambat (titik siku)")

# Plot elbow
plt.plot(list(hasil_elbow.keys()), list(hasil_elbow.values()), "bo-")
plt.xlabel("Jumlah Cluster (k)")
plt.ylabel("Inertia")
plt.title("Metode Elbow — Mencari k Optimal")
plt.savefig("plot_elbow.png")
plt.clf()
print("\nplot_elbow.png disimpan.")

# Scatter plot hasil clustering
warna = ["red" if l == 0 else "blue" for l in model.labels_]
pusat = model.cluster_centers_

plt.scatter(titik[:, 0], titik[:, 1], c=warna, s=100, label="Data")
plt.scatter(pusat[:, 0], pusat[:, 1], c="black", s=200, marker="X", label="Pusat cluster")
for i, (x, y) in enumerate(titik):
    plt.annotate(f"P{i+1}", (x, y), textcoords="offset points", xytext=(5, 5))
plt.title("Hasil K-Means (k=2)")
plt.legend()
plt.savefig("plot_kmeans.png")
plt.clf()
print("plot_kmeans.png disimpan.")

# 3. RANGKUMAN

# - K-Means mengelompokkan data ke k cluster berdasarkan kedekatan ke pusat cluster.
# - Jumlah cluster (k) harus ditentukan di awal — gunakan metode elbow untuk membantu memilih.
# - Inertia mengukur kualitas clustering — semakin kecil semakin baik.
# - model.labels_ menyimpan label cluster setiap titik data.
# - model.predict() digunakan untuk mengelompokkan titik baru tanpa melatih ulang.