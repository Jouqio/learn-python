# 1. KONSEP

# Tiga ukuran pemusatan data yang paling dasar dalam statistik:
#
# - Mean   (rata-rata) → jumlah semua nilai dibagi banyak data
# - Median (nilai tengah) → nilai di posisi tengah setelah data diurutkan
# - Modus  (mode) → nilai yang paling sering muncul
#
# Kapan menggunakan masing-masing:
# - Mean   → data tidak punya nilai ekstrem (outlier)
# - Median → data punya outlier (lebih tahan terhadap nilai ekstrem)
# - Modus  → ingin tahu nilai yang paling umum/sering muncul

# 2. CONTOH

from statistics import mean, median, mode
import numpy as np

nilai = [70, 85, 90, 85, 60, 85]

# Menggunakan modul statistics bawaan Python
print("=== Modul statistics ===")
print(f"Mean   : {mean(nilai)}")      # 79.16...
print(f"Median : {median(nilai)}")    # 85.0
print(f"Modus  : {mode(nilai)}")      # 85 — paling sering muncul

# Menggunakan NumPy
print("\n=== NumPy ===")
data = np.array(nilai)
print(f"Mean   : {np.mean(data):.2f}")
print(f"Median : {np.median(data)}")

# NumPy tidak punya mode — gunakan scipy atau hitung manual
from collections import Counter
paling_sering = Counter(nilai).most_common(1)[0]
print(f"Modus  : {paling_sering[0]} (muncul {paling_sering[1]}x)")

# Pengaruh outlier terhadap mean vs median
print("\n=== Outlier ===")
gaji = [3000000, 3500000, 4000000, 3200000, 50000000]  # 50jt = outlier

print(f"Mean   : Rp {mean(gaji):,.0f}")    # ditarik jauh oleh outlier
print(f"Median : Rp {median(gaji):,.0f}")  # lebih representatif

# Fungsi ringkasan pemusatan data
def laporan_pemusatan(data):
    frekuensi = Counter(data)
    modus = frekuensi.most_common(1)[0][0]
    return {
        "mean"  : round(mean(data), 2),
        "median": median(data),
        "modus" : modus,
    }

hasil = laporan_pemusatan(nilai)
for ukuran, nilai_ukuran in hasil.items():
    print(f"{ukuran:<8}: {nilai_ukuran}")

# 3. RANGKUMAN

# - Mean adalah rata-rata — sensitif terhadap nilai ekstrem (outlier).
# - Median adalah nilai tengah — lebih stabil saat ada outlier.
# - Modus adalah nilai yang paling sering muncul.
# - Gunakan modul statistics untuk data sederhana, NumPy untuk array besar.