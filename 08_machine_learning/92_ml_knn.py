# 1. KONSEP

# KNN (K-Nearest Neighbors) mengklasifikasikan titik baru
# berdasarkan mayoritas kelas dari k tetangga terdekatnya.
#
# Cara kerjanya:
# 1. Hitung jarak titik baru ke semua titik data latih
# 2. Ambil k titik terdekat
# 3. Prediksi = kelas yang paling banyak di antara k tetangga itu
#
# Parameter penting:
# - k kecil (k=1) → model sangat mengikuti data, rentan overfitting
# - k besar        → model lebih halus tapi bisa underfitting
#
# Peringatan: KNN sangat sensitif terhadap skala fitur
# → selalu lakukan feature scaling sebelum menggunakan KNN

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Data latih: [x, y] → kelas 0 atau 1
X_latih = [[4, 21], [5, 19], [10, 24], [4, 17], [3, 16], [11, 25]]
y_latih = [0, 0, 1, 0, 0, 1]

# KNN dasar dengan k=3
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_latih, y_latih)

titik_baru = [[8, 21]]
print("=== KNN Dasar (k=3) ===")
print(f"Prediksi untuk {titik_baru[0]}: kelas {model.predict(titik_baru)[0]}")

# Perbandingan berbagai nilai k
print("\n=== Pengaruh Nilai k ===")
for k in [1, 3, 5, len(X_latih)]:
    m = KNeighborsClassifier(n_neighbors=k)
    m.fit(X_latih, y_latih)
    pred = m.predict(titik_baru)[0]
    akurasi = accuracy_score(y_latih, m.predict(X_latih))
    print(f"k={k:<3} → prediksi: {pred}, akurasi latih: {akurasi:.2f}")

# Mengapa scaling penting untuk KNN
print("\n=== Pentingnya Feature Scaling untuk KNN ===")
X_berskala_beda = np.array([
    [1, 1000],   # fitur 1: satuan kecil, fitur 2: satuan besar
    [2, 2000],
    [3, 3000],
])
y_berskala = [0, 0, 1]

# Tanpa scaling — jarak didominasi fitur dengan nilai besar
model_tanpa = KNeighborsClassifier(n_neighbors=2)
model_tanpa.fit(X_berskala_beda, y_berskala)

# Dengan scaling — semua fitur punya pengaruh setara
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_berskala_beda)
model_dengan = KNeighborsClassifier(n_neighbors=2)
model_dengan.fit(X_scaled, y_berskala)

print("Tanpa scaling: jarak didominasi fitur bernilai besar")
print("Dengan scaling: semua fitur punya pengaruh setara")
print("→ Selalu scaling sebelum menggunakan KNN")

# Scatter plot titik latih + titik baru
warna = ["steelblue" if k == 0 else "salmon" for k in y_latih]
X_arr = np.array(X_latih)

plt.scatter(X_arr[:, 0], X_arr[:, 1], c=warna, s=100, label="Data latih")
plt.scatter(titik_baru[0][0], titik_baru[0][1],
    c="green", s=200, marker="*", label="Titik baru", zorder=5)

for i, (x, y) in enumerate(X_latih):
    plt.annotate(f"P{i+1}(kelas {y_latih[i]})", (x, y),
        textcoords="offset points", xytext=(5, 5), fontsize=8)

plt.title("KNN — Titik Data dan Titik yang Diprediksi")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.savefig("plot_knn.png")
plt.clf()
print("\nplot_knn.png disimpan.")

# Fungsi reusable — cari nilai k terbaik
def cari_k_terbaik(X_latih, y_latih, X_uji, y_uji, rentang_k):
    hasil = {}
    for k in rentang_k:
        m = KNeighborsClassifier(n_neighbors=k)
        m.fit(X_latih, y_latih)
        hasil[k] = round(accuracy_score(y_uji, m.predict(X_uji)), 4)

    k_terbaik = max(hasil, key=hasil.get)
    print("=== Cari k Terbaik ===")
    for k, akurasi in hasil.items():
        tanda = " ← terbaik" if k == k_terbaik else ""
        print(f"k={k:<3} → akurasi: {akurasi}{tanda}")
    return k_terbaik

X_arr   = np.array(X_latih)
k_terbaik = cari_k_terbaik(
    X_arr[:4], y_latih[:4],
    X_arr[4:], y_latih[4:],
    rentang_k=range(1, 4)
)
print(f"\nNilai k terbaik: {k_terbaik}")

# 3. RANGKUMAN

# - KNN memprediksi kelas berdasarkan mayoritas kelas dari k tetangga terdekat.
# - k kecil → lebih sensitif terhadap noise; k besar → prediksi lebih halus.
# - SELALU lakukan feature scaling sebelum KNN — jarak sangat terpengaruh skala.
# - KNN tidak membangun model eksplisit — semua perhitungan saat prediksi.
# - Coba beberapa nilai k dan pilih yang memberikan akurasi terbaik di data uji.