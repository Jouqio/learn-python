# 1. KONSEP

# Distribusi Normal (Gaussian) adalah distribusi berbentuk lonceng
# yang simetris di sekitar rata-ratanya.
#
# Didefinisikan oleh dua parameter:
# - loc   (mean) → pusat / puncak kurva
# - scale (std)  → seberapa lebar kurva menyebar
#
# Aturan 68-95-99.7:
# - ~68% data berada dalam ±1 standar deviasi dari mean
# - ~95% data berada dalam ±2 standar deviasi dari mean
# - ~99.7% data berada dalam ±3 standar deviasi dari mean
#
# Contoh nyata: tinggi badan, nilai ujian, tekanan darah

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=42)

# Membuat data distribusi normal
data = rng.normal(loc=5.0, scale=1.0, size=1000)

print("=== Distribusi Normal (mean=5, std=1) ===")
print(f"Mean sampel : {np.mean(data):.2f}")
print(f"Std sampel  : {np.std(data):.2f}")

# Histogram distribusi normal
plt.hist(data, bins=30, color="steelblue", edgecolor="white")
plt.title("Distribusi Normal (mean=5, std=1)")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.savefig("plot_normal.png")
plt.clf()
print("plot_normal.png disimpan.")

# Membandingkan dua distribusi normal dengan mean berbeda
data_a = rng.normal(loc=50, scale=10, size=500)  # mean=50
data_b = rng.normal(loc=70, scale=10, size=500)  # mean=70

plt.hist(data_a, bins=25, alpha=0.6, label="mean=50", color="steelblue")
plt.hist(data_b, bins=25, alpha=0.6, label="mean=70", color="salmon")
plt.title("Perbandingan Dua Distribusi Normal")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.legend()
plt.savefig("plot_normal_perbandingan.png")
plt.clf()
print("plot_normal_perbandingan.png disimpan.")

# Pengaruh ukuran sampel terhadap akurasi mean dan std
print("\n=== Akurasi Meningkat Seiring Jumlah Sampel ===")
for n in [10, 100, 1000, 10000]:
    sampel = rng.normal(loc=0, scale=1, size=n)
    print(f"n={n:<6} → mean: {np.mean(sampel):+.4f}, std: {np.std(sampel):.4f}")

# Fungsi: menghitung persentase nilai dalam ±1 standar deviasi
def persen_dalam_1_std(data):
    mean = np.mean(data)
    std  = np.std(data)
    dalam = np.sum((data >= mean - std) & (data <= mean + std))
    persen = (dalam / len(data)) * 100
    return round(persen, 2)

data_uji = rng.normal(loc=0, scale=1, size=10000)
print(f"\nNilai dalam ±1 std: {persen_dalam_1_std(data_uji)}%")
print("(Nilai teori: ~68%)")

# 3. RANGKUMAN

# - Distribusi normal berbentuk lonceng, simetris di sekitar mean.
# - Diatur oleh mean (pusat) dan std (lebar kurva).
# - Aturan 68-95-99.7: sebagian besar data berkumpul dekat mean.
# - Semakin besar ukuran sampel, mean dan std sampel mendekati nilai sebenarnya.
# - Gunakan rng.normal(loc, scale, size) untuk membuat data normal.