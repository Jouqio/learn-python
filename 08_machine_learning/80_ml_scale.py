# 1. KONSEP

# Fitur dalam dataset sering punya skala yang sangat berbeda.
# Contoh: ukuran_mesin (0.9–2.5) vs berat_kendaraan (1600–2500)
#
# Perbedaan skala ini bisa membuat model ML bias — fitur bernilai
# besar dianggap "lebih penting" padahal belum tentu begitu.
#
# Solusi: scaling (penskalaan) agar semua fitur punya rentang serupa.
#
# Dua metode yang sering dipakai:
# - StandardScaler  → transformasi ke mean=0, std=1
# - MinMaxScaler    → transformasi ke rentang [0, 1]
#
# Aturan penting:
# - fit() hanya pada data latih (training data)
# - transform() pada data latih DAN data baru (test/prediksi)

# 2. CONTOH

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Data: [ukuran_mesin, berat_kendaraan]
X = np.array([
    [0.9, 1600],
    [1.4, 1900],
    [2.0, 2200],
    [1.2, 1700],
    [1.8, 2000],
    [2.5, 2500],
])

# StandardScaler — transformasi ke mean=0, std=1
scaler_std = StandardScaler()
X_std = scaler_std.fit_transform(X)

print("=== StandardScaler ===")
print(f"Mean asal    : {scaler_std.mean_}")
print(f"Std asal     : {scaler_std.scale_}")
print(f"Hasil scaling:\n{X_std.round(3)}")

# MinMaxScaler — transformasi ke rentang [0, 1]
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)

print("\n=== MinMaxScaler ===")
print(f"Hasil scaling:\n{X_minmax.round(3)}")

# Scaling data baru menggunakan scaler yang sudah di-fit
# JANGAN fit ulang — gunakan transform saja
data_baru = np.array([[1.6, 1800]])
data_baru_scaled = scaler_std.transform(data_baru)
print(f"\nData baru asli   : {data_baru}")
print(f"Data baru scaled : {data_baru_scaled.round(3)}")

# Perbandingan StandardScaler vs MinMaxScaler
print("\n=== Perbandingan ===")
print(f"{'Asli':<20} {'Standard':<20} {'MinMax'}")
for asli, std, mm in zip(X, X_std, X_minmax):
    print(f"{str(asli):<20} {str(std.round(2)):<20} {mm.round(2)}")

# Fungsi reusable — fit pada data latih, transform keduanya
def skala_data(X_latih, X_baru):
    scaler = StandardScaler()
    X_latih_scaled = scaler.fit_transform(X_latih)  # fit + transform data latih
    X_baru_scaled  = scaler.transform(X_baru)        # transform saja data baru
    return X_latih_scaled, X_baru_scaled, scaler

X_latih_s, X_baru_s, scaler = skala_data(X, data_baru)

print(f"\nData latih (scaled):\n{X_latih_s.round(3)}")
print(f"Data baru  (scaled): {X_baru_s.round(3)}")

# 3. RANGKUMAN

# - Scaling diperlukan saat fitur punya rentang nilai yang sangat berbeda.
# - StandardScaler → mean=0, std=1 (cocok untuk data dengan distribusi normal).
# - MinMaxScaler   → rentang [0, 1] (cocok saat butuh batas nilai yang jelas).
# - Selalu fit scaler hanya pada data latih, lalu transform data latih dan data baru.
# - Jangan fit ulang scaler saat menerima data baru — gunakan scaler yang sama.