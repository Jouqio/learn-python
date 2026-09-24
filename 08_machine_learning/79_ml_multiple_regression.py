# 1. KONSEP

# Regresi berganda memprediksi satu nilai target (y)
# menggunakan DUA atau lebih fitur input (X).
#
# Persamaan: y = b0 + b1*x1 + b2*x2 + ... + bn*xn
#
# Koefisien (coef_) menunjukkan pengaruh setiap fitur:
# - Koefisien positif → fitur naik, prediksi naik
# - Koefisien negatif → fitur naik, prediksi turun
# - Nilai koefisien besar → fitur berpengaruh lebih besar

# 2. CONTOH

from sklearn import linear_model
import numpy as np

# Data: [ukuran_mesin, berat_kendaraan] → emisi CO2
X_latih = [
    [0.9, 1600],
    [1.4, 1900],
    [2.0, 2200],
    [1.2, 1700],
    [1.8, 2000],
    [2.5, 2500],
]
y_latih = [95, 110, 140, 100, 128, 160]  # emisi CO2

# Membuat dan melatih model
model = linear_model.LinearRegression()
model.fit(X_latih, y_latih)

print("=== Regresi Berganda: 2 Fitur ===")
print(f"Koefisien    : {model.coef_}")
print(f"  ukuran_mesin → {model.coef_[0]:.4f}")
print(f"  berat        → {model.coef_[1]:.4f}")
print(f"Intercept    : {model.intercept_:.4f}")

# Prediksi untuk data baru
data_baru = [[1.6, 1800]]
prediksi  = model.predict(data_baru)
print(f"\nPrediksi emisi untuk mesin=1.6, berat=1800: {prediksi[0]:.1f}")

# Menambahkan fitur ketiga — jumlah silinder
X_latih_3 = [
    [0.9, 1600, 4],
    [1.4, 1900, 4],
    [2.0, 2200, 6],
    [1.2, 1700, 4],
    [1.8, 2000, 6],
    [2.5, 2500, 8],
]

model_3 = linear_model.LinearRegression()
model_3.fit(X_latih_3, y_latih)

print("\n=== Regresi Berganda: 3 Fitur ===")
print(f"Koefisien    : {model_3.coef_}")
print(f"  ukuran_mesin → {model_3.coef_[0]:.4f}")
print(f"  berat        → {model_3.coef_[1]:.4f}")
print(f"  silinder     → {model_3.coef_[2]:.4f}")

# Perbandingan prediksi sebelum dan sesudah fitur ketiga
data_baru_2 = [[1.6, 1800]]
data_baru_3 = [[1.6, 1800, 4]]

pred_2 = model.predict(data_baru_2)[0]
pred_3 = model_3.predict(data_baru_3)[0]

print(f"\nPrediksi dengan 2 fitur : {pred_2:.1f}")
print(f"Prediksi dengan 3 fitur : {pred_3:.1f}")

# Fungsi reusable — latih model dan prediksi sekaligus
def latih_dan_prediksi(X_latih, y_latih, X_baru):
    model = linear_model.LinearRegression()
    model.fit(X_latih, y_latih)
    hasil = model.predict(X_baru)
    return [round(h, 2) for h in hasil]

hasil = latih_dan_prediksi(X_latih, y_latih, [[1.6, 1800], [2.2, 2300]])
print(f"\nHasil fungsi reusable: {hasil}")

# 3. RANGKUMAN

# - Regresi berganda menggunakan beberapa fitur sekaligus untuk prediksi.
# - model.coef_ menunjukkan bobot/pengaruh setiap fitur.
# - model.intercept_ adalah nilai dasar saat semua fitur bernilai 0.
# - Menambah fitur relevan bisa meningkatkan akurasi prediksi.
# - Gunakan LinearRegression() dari sklearn untuk regresi berganda.