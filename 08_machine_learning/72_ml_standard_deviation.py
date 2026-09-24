# 1. KONSEP

# Standar deviasi mengukur seberapa jauh data menyebar dari rata-ratanya.
#
# - Standar deviasi KECIL → data berkumpul dekat dengan rata-rata (seragam)
# - Standar deviasi BESAR → data menyebar jauh dari rata-rata (bervariasi)
#
# Hubungan dengan varians:
# - Varians   = rata-rata kuadrat jarak setiap nilai dari mean
# - Standar deviasi = akar kuadrat dari varians

# 2. CONTOH

import numpy as np
from statistics import stdev, variance

data = np.array([32, 111, 138, 28, 59, 77, 97])

# Menggunakan NumPy
print("=== NumPy ===")
print(f"Mean             : {np.mean(data):.2f}")
print(f"Standar Deviasi  : {np.std(data):.2f}")
print(f"Varians          : {np.var(data):.2f}")
print(f"Std² = Varians   : {np.std(data)**2:.2f}")  # std² = varians

# Menggunakan modul statistics bawaan Python
print("\n=== Modul statistics ===")
data_list = data.tolist()
print(f"Standar Deviasi  : {stdev(data_list):.2f}")   # ddof=1 (sampel)
print(f"Varians          : {variance(data_list):.2f}")

# Membandingkan dua dataset dengan mean sama tapi penyebaran berbeda
print("\n=== Perbandingan Penyebaran ===")
data_seragam  = np.array([48, 49, 50, 51, 52])   # menyebar sedikit
data_bervariasi = np.array([10, 30, 50, 70, 90]) # menyebar jauh

print(f"Data seragam    — mean: {np.mean(data_seragam):.1f}, std: {np.std(data_seragam):.2f}")
print(f"Data bervariasi — mean: {np.mean(data_bervariasi):.1f}, std: {np.std(data_bervariasi):.2f}")
print("Mean sama, tapi penyebaran sangat berbeda.")

# Deteksi outlier — nilai yang lebih dari 2 standar deviasi dari mean
def deteksi_outlier(data):
    mean = np.mean(data)
    std  = np.std(data)
    batas_atas  = mean + 2 * std
    batas_bawah = mean - 2 * std

    print(f"Mean      : {mean:.2f}")
    print(f"Std Dev   : {std:.2f}")
    print(f"Batas     : {batas_bawah:.2f} — {batas_atas:.2f}")

    outlier = [x for x in data if x < batas_bawah or x > batas_atas]
    normal  = [x for x in data if batas_bawah <= x <= batas_atas]

    print(f"Normal    : {normal}")
    print(f"Outlier   : {outlier}")

nilai = np.array([50, 52, 49, 53, 51, 48, 95, 50, 47, 5])
deteksi_outlier(nilai)

# 3. RANGKUMAN

# - Standar deviasi mengukur seberapa jauh data menyebar dari mean.
# - Std kecil → data seragam; std besar → data sangat bervariasi.
# - Varians = std² — keduanya mengukur penyebaran, std lebih mudah dibaca.
# - Nilai lebih dari 2 std dari mean umumnya dianggap outlier.
# - Gunakan np.std() untuk array NumPy, stdev() dari modul statistics untuk list biasa.