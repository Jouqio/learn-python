# 1. KONSEP

# Persentil menunjukkan nilai di bawah mana sejumlah persen data berada.
#
# Contoh mudah:
# - Persentil ke-75 = 80 → artinya 75% data bernilai di bawah 80
# - Persentil ke-50 = median (nilai tengah dataset)
#
# Persentil penting yang sering dipakai:
# - Q1 (persentil ke-25) → batas bawah kuartil
# - Q2 (persentil ke-50) → median
# - Q3 (persentil ke-75) → batas atas kuartil
# - IQR = Q3 - Q1        → rentang antar kuartil (ukuran penyebaran tengah)

# 2. CONTOH

import numpy as np

usia = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Persentil dasar
print(f"Persentil ke-25  : {np.percentile(usia, 25)}")
print(f"Persentil ke-50  : {np.percentile(usia, 50)}")   # sama dengan median
print(f"Persentil ke-75  : {np.percentile(usia, 75)}")
print(f"Persentil ke-90  : {np.percentile(usia, 90)}")

# Q1, Q2, Q3, dan IQR
q1  = np.percentile(usia, 25)
q2  = np.percentile(usia, 50)
q3  = np.percentile(usia, 75)
iqr = q3 - q1

print(f"\nQ1  (ke-25) : {q1}")
print(f"Q2  (ke-50) : {q2}")
print(f"Q3  (ke-75) : {q3}")
print(f"IQR (Q3-Q1) : {iqr}")

# Deteksi outlier menggunakan metode IQR
batas_bawah = q1 - 1.5 * iqr
batas_atas  = q3 + 1.5 * iqr

print(f"\nBatas bawah : {batas_bawah}")
print(f"Batas atas  : {batas_atas}")

outlier = [x for x in usia if x < batas_bawah or x > batas_atas]
normal  = [x for x in usia if batas_bawah <= x <= batas_atas]

print(f"Normal      : {sorted(normal)}")
print(f"Outlier     : {sorted(outlier)}")

# Fungsi ringkasan persentil
def ringkasan_persentil(data):
    q1  = np.percentile(data, 25)
    q2  = np.percentile(data, 50)
    q3  = np.percentile(data, 75)
    iqr = q3 - q1
    return {
        "Q1 (ke-25)" : q1,
        "Q2 (ke-50)" : q2,
        "Q3 (ke-75)" : q3,
        "IQR"        : iqr,
    }

nilai_ujian = [55, 60, 65, 70, 72, 75, 78, 80, 85, 90, 95, 98]
hasil = ringkasan_persentil(nilai_ujian)

print("\n=== Ringkasan Persentil Nilai Ujian ===")
for label, nilai in hasil.items():
    print(f"{label:<12}: {nilai}")

# 3. RANGKUMAN

# - Persentil ke-N artinya N% data berada di bawah nilai tersebut.
# - Q1, Q2, Q3 adalah persentil ke-25, 50, dan 75.
# - IQR = Q3 - Q1 mengukur penyebaran 50% data di tengah.
# - Outlier terdeteksi jika nilainya di luar Q1 - 1.5×IQR atau Q3 + 1.5×IQR.
# - Gunakan np.percentile(data, n) untuk menghitung persentil ke-n.