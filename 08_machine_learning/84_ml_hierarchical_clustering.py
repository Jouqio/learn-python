# 1. KONSEP

# Hierarchical Clustering adalah metode pengelompokan data yang
# membangun hierarki cluster (kelompok) secara bertahap.
#
# Cara kerjanya:
# - Mulai dengan setiap titik sebagai cluster sendiri
# - Gabungkan dua cluster terdekat secara berulang
# - Hasilnya berupa pohon cluster yang disebut dendrogram
#
# Metode linkage (cara mengukur jarak antar cluster):
# - ward     → meminimalkan varians dalam cluster (paling umum)
# - single   → jarak titik terdekat antar cluster
# - complete → jarak titik terjauh antar cluster
#
# Keunggulan: tidak perlu menentukan jumlah cluster dari awal

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram

# Data titik 2D
titik = np.array([
    [4, 21], [5, 19], [10, 24],
    [4, 17], [3, 16], [11, 25], [14, 24]
])

# Membuat linkage matrix — "peta" bagaimana cluster terbentuk
linkage_matrix = linkage(titik, method="ward")

# Membagi menjadi 2 cluster
cluster_2 = fcluster(linkage_matrix, t=2, criterion="maxclust")
print("=== 2 Cluster ===")
print(f"Penugasan cluster: {cluster_2}")
for i, (titik_xy, kluster) in enumerate(zip(titik, cluster_2)):
    print(f"  Titik {i+1} {titik_xy} → Cluster {kluster}")

# Membagi menjadi 3 cluster
cluster_3 = fcluster(linkage_matrix, t=3, criterion="maxclust")
print("\n=== 3 Cluster ===")
print(f"Penugasan cluster: {cluster_3}")

# Perbandingan metode linkage
print("\n=== Perbandingan Metode Linkage ===")
for metode in ["ward", "single", "complete"]:
    lm = linkage(titik, method=metode)
    cl = fcluster(lm, t=2, criterion="maxclust")
    print(f"{metode:<10}: {cl}")

print("\nKeterangan:")
print("  ward     → meminimalkan varians, cluster cenderung seragam")
print("  single   → mudah digabung jika ada 'jembatan' antar cluster")
print("  complete → lebih konservatif, cluster lebih kompak")

# Visualisasi dendrogram
plt.figure(figsize=(8, 4))
dendrogram(linkage_matrix)
plt.title("Dendrogram — Hierarchical Clustering")
plt.xlabel("Indeks Titik Data")
plt.ylabel("Jarak")
plt.savefig("plot_dendrogram.png")
plt.clf()
print("\nplot_dendrogram.png disimpan.")

# Scatter plot dengan warna cluster
warna_cluster = ["red" if c == 1 else "blue" for c in cluster_2]
plt.scatter(titik[:, 0], titik[:, 1], c=warna_cluster, s=100)
for i, (x, y) in enumerate(titik):
    plt.annotate(f"P{i+1}", (x, y), textcoords="offset points", xytext=(5, 5))
plt.title("Hasil 2 Cluster")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("plot_cluster_hierarkis.png")
plt.clf()
print("plot_cluster_hierarkis.png disimpan.")

# Fungsi reusable — kelompokkan titik dan kembalikan per cluster
def kelompokkan_titik(data, jumlah_cluster, metode="ward"):
    lm  = linkage(data, method=metode)
    cl  = fcluster(lm, t=jumlah_cluster, criterion="maxclust")
    hasil = {}
    for i in range(1, jumlah_cluster + 1):
        hasil[f"Cluster {i}"] = data[cl == i].tolist()
    return hasil

hasil = kelompokkan_titik(titik, jumlah_cluster=2)
print("\n=== Titik per Cluster ===")
for nama, anggota in hasil.items():
    print(f"{nama}: {anggota}")

# 3. RANGKUMAN

# - Hierarchical clustering mengelompokkan data tanpa perlu menentukan jumlah cluster di awal.
# - linkage() membangun hierarki cluster; fcluster() memotongnya menjadi n cluster.
# - Metode ward paling umum digunakan karena menghasilkan cluster yang seragam.
# - Dendrogram memvisualisasikan bagaimana cluster terbentuk secara bertahap.
# - Gunakan criterion="maxclust" untuk menentukan jumlah cluster yang diinginkan.