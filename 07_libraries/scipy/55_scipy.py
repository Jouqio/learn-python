# 1. KONSEP

# SciPy (Scientific Python) adalah library yang dibangun di atas NumPy.
# Berisi banyak alat untuk perhitungan sains dan analisis data.
#
# Instalasi: pip install scipy
#
# Hal-hal yang dibahas:
# constants         → konstanta fisika (kecepatan cahaya, dll.)
# optimize.minimize → mencari nilai minimum sebuah fungsi
# sparse.csr_matrix → menyimpan matriks yang isinya banyak angka nol
# distance          → menghitung jarak antar titik
# interp1d          → memperkirakan nilai di antara data yang diketahui
# stats.ttest_ind   → uji t untuk membandingkan dua kelompok data

# 2. CONTOH

import numpy as np
from scipy import constants, optimize, sparse, interpolate, stats
from scipy.spatial import distance

# Konstanta fisika
print("Kecepatan cahaya:", constants.speed_of_light)
print("Percepatan gravitasi:", constants.g)
print("Konstanta Planck:", constants.Planck)

# Optimasi — mencari nilai minimum fungsi
def fungsi(x):
    return x ** 2 + 5 * x + 4

hasil = optimize.minimize(fungsi, x0=0)
print("Nilai minimum ada di x =", round(hasil.x[0], 3))

# Sparse matrix — hanya menyimpan angka yang bukan nol
padat = np.array([[0, 0, 3], [4, 0, 0], [0, 0, 5]])
matriks_sparse = sparse.csr_matrix(padat)
print("Sparse matrix:")
print(matriks_sparse)

# Jarak antar dua titik
titik_a = (0, 0)
titik_b = (3, 4)
print("Jarak Euclidean:", distance.euclidean(titik_a, titik_b))
print("Jarak Manhattan:", distance.cityblock(titik_a, titik_b))

# Interpolasi — memperkirakan nilai di antara data
x_diketahui = np.array([0, 1, 2, 3])
y_diketahui = np.array([0, 1, 4, 9])

fungsi_interp = interpolate.interp1d(x_diketahui, y_diketahui)
print("Nilai di x=1.5:", fungsi_interp(1.5))

# Uji t — membandingkan dua kelompok data
kelompok_a = [23, 25, 21, 22, 24]
kelompok_b = [30, 28, 27, 29, 31]

t_stat, p_value = stats.ttest_ind(kelompok_a, kelompok_b)
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_value:.4f}")

# 3. RANGKUMAN

# - constants menyediakan konstanta fisika siap pakai.
# - optimize.minimize() mencari nilai x yang membuat fungsi paling kecil.
# - sparse.csr_matrix() menghemat memori untuk matriks yang banyak berisi nol.
# - distance.euclidean() dan distance.cityblock() menghitung jarak antar titik.
# - interp1d() memperkirakan nilai di antara data yang sudah diketahui.
# - stats.ttest_ind() membandingkan dua kelompok; p-value kecil (< 0.05) berarti perbedaan signifikan.