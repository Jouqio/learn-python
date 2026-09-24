# 1. KONSEP

# Distribusi data menggambarkan bagaimana nilai-nilai dalam dataset tersebar.
# Sebelum menggunakan data nyata, kita sering membuat data simulasi
# untuk berlatih dan menguji metode statistik.
#
# Dua distribusi yang sering digunakan:
# - Distribusi Uniform  → semua nilai punya peluang sama untuk muncul
# - Distribusi Normal   → nilai mengelompok di sekitar rata-rata (bentuk lonceng)
#
# Random seed → membuat data acak yang bisa direproduksi ulang dengan hasil sama

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Random seed — memastikan hasil acak selalu sama setiap dijalankan
rng = np.random.default_rng(seed=42)

# Distribusi Uniform — nilai tersebar merata antara batas bawah dan atas
data_uniform = rng.uniform(0.0, 5.0, 250)

print("=== Distribusi Uniform ===")
print(f"Mean    : {np.mean(data_uniform):.3f}")
print(f"Std Dev : {np.std(data_uniform):.3f}")
print(f"Min     : {data_uniform.min():.2f}")
print(f"Max     : {data_uniform.max():.2f}")

# Distribusi Normal — nilai mengelompok di sekitar mean
data_normal = rng.normal(loc=50, scale=10, size=250)  # mean=50, std=10

print("\n=== Distribusi Normal ===")
print(f"Mean    : {np.mean(data_normal):.3f}")
print(f"Std Dev : {np.std(data_normal):.3f}")
print(f"Min     : {data_normal.min():.2f}")
print(f"Max     : {data_normal.max():.2f}")

# Membandingkan dua distribusi lewat histogram
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].hist(data_uniform, bins=20, color="steelblue")
axes[0].set_title("Distribusi Uniform (0–5)")
axes[0].set_xlabel("Nilai")
axes[0].set_ylabel("Frekuensi")

axes[1].hist(data_normal, bins=20, color="salmon")
axes[1].set_title("Distribusi Normal (mean=50, std=10)")
axes[1].set_xlabel("Nilai")

plt.tight_layout()
plt.savefig("plot_distribusi.png")
plt.clf()
print("\nplot_distribusi.png disimpan.")

# Fungsi ringkasan statistik dari data simulasi
def ringkasan_distribusi(n, batas_bawah=0, batas_atas=100, seed=42):
    rng  = np.random.default_rng(seed=seed)
    data = rng.uniform(batas_bawah, batas_atas, n)
    return {
        "n sampel" : n,
        "mean"     : round(np.mean(data), 2),
        "std"      : round(np.std(data), 2),
        "min"      : round(data.min(), 2),
        "max"      : round(data.max(), 2),
    }

hasil = ringkasan_distribusi(500)
print("\n=== Ringkasan Distribusi (500 sampel) ===")
for label, nilai in hasil.items():
    print(f"{label:<10}: {nilai}")

# 3. RANGKUMAN

# - Distribusi data menunjukkan bagaimana nilai tersebar dalam dataset.
# - Distribusi uniform → nilai tersebar merata; distribusi normal → mengelompok di tengah.
# - Gunakan random seed agar data acak bisa direproduksi dengan hasil sama.
# - np.random.default_rng(seed) lebih modern dan direkomendasikan daripada np.random.seed().
# - Histogram adalah cara terbaik untuk memvisualisasikan bentuk distribusi data.