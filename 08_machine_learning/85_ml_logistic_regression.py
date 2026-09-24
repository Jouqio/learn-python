# 1. KONSEP

# Regresi logistik digunakan untuk memprediksi hasil BINER
# (dua kemungkinan: ya/tidak, lulus/tidak, sakit/sehat).
#
# Berbeda dari regresi linear yang menghasilkan angka kontinu,
# regresi logistik menghasilkan PROBABILITAS (0.0 hingga 1.0).
#
# Cara kerjanya:
# - Menghitung probabilitas → nilai antara 0 dan 1
# - Jika probabilitas >= 0.5 → prediksi kelas 1 (positif)
# - Jika probabilitas < 0.5  → prediksi kelas 0 (negatif)
#
# Kurva yang dihasilkan berbentuk S (sigmoid), bukan garis lurus.

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Data: jam belajar vs hasil ujian (0=tidak lulus, 1=lulus)
jam_belajar = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
hasil       = [0, 0, 0, 1, 1, 1, 1, 1]

# Membuat dan melatih model
model = LogisticRegression()
model.fit(jam_belajar, hasil)

# Prediksi probabilitas
prob = model.predict_proba([[3.5]])[0]
print("=== Prediksi Probabilitas ===")
print(f"Belajar 3.5 jam → tidak lulus: {prob[0]:.2f}, lulus: {prob[1]:.2f}")

# Prediksi kelas langsung
print("\n=== Prediksi Kelas ===")
for jam in [2, 4, 6]:
    p     = model.predict_proba([[jam]])[0][1]
    kelas = model.predict([[jam]])[0]
    label = "Lulus" if kelas == 1 else "Tidak Lulus"
    print(f"Belajar {jam} jam → probabilitas lulus: {p:.2f} → {label}")

# Akurasi model pada data latih
akurasi = accuracy_score(hasil, model.predict(jam_belajar))
print(f"\nAkurasi pada data latih: {akurasi:.2f}")

# Visualisasi kurva sigmoid
x_range = np.linspace(0, 10, 300).reshape(-1, 1)
y_prob  = model.predict_proba(x_range)[:, 1]

plt.scatter(jam_belajar, hasil, color="steelblue", zorder=5, label="Data asli")
plt.plot(x_range, y_prob, color="salmon", label="Kurva probabilitas")
plt.axhline(y=0.5, color="gray", linestyle="--", label="Batas keputusan (0.5)")
plt.xlabel("Jam Belajar")
plt.ylabel("Probabilitas Lulus")
plt.title("Regresi Logistik — Kurva Sigmoid")
plt.legend()
plt.savefig("plot_regresi_logistik.png")
plt.clf()
print("\nplot_regresi_logistik.png disimpan.")

# Fungsi reusable — prediksi probabilitas lulus
def prediksi_probabilitas_lulus(jam, jam_data, hasil_data):
    X = np.array(jam_data).reshape(-1, 1)
    model = LogisticRegression()
    model.fit(X, hasil_data)
    prob = model.predict_proba([[jam]])[0][1]
    return round(prob, 4)

prob_35 = prediksi_probabilitas_lulus(3.5, [1,2,3,4,5,6,7,8], hasil)
prob_60 = prediksi_probabilitas_lulus(6.0, [1,2,3,4,5,6,7,8], hasil)
print(f"\nProbabilitas lulus (3.5 jam): {prob_35}")
print(f"Probabilitas lulus (6.0 jam): {prob_60}")

# 3. RANGKUMAN

# - Regresi logistik memprediksi probabilitas untuk hasil biner (0 atau 1).
# - Hasilnya berupa nilai antara 0 dan 1, bukan angka bebas.
# - Gunakan predict_proba() untuk probabilitas, predict() untuk kelas langsung.
# - Batas keputusan default adalah 0.5 — di atas itu → kelas 1, di bawah → kelas 0.
# - Kurva berbentuk S (sigmoid) karena probabilitas tidak bisa di luar rentang [0, 1].