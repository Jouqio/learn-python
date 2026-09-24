# 1. KONSEP

# Regresi polinomial digunakan saat hubungan antara x dan y
# membentuk kurva, bukan garis lurus.
#
# Persamaan: y = ax² + bx + c  (derajat 2)
#            y = ax³ + bx² + cx + d  (derajat 3)
#
# Derajat (degree) menentukan seberapa bengkok kurvanya:
# - Derajat 1 → garis lurus (sama dengan regresi linear)
# - Derajat 2 → kurva parabola
# - Derajat 3 → kurva lebih fleksibel
#
# Peringatan: derajat terlalu tinggi → overfitting
# (model mengikuti noise data, buruk untuk prediksi data baru)

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75])

# Membuat model polinomial derajat 2 dan 3
model_d2 = np.poly1d(np.polyfit(x, y, 2))
model_d3 = np.poly1d(np.polyfit(x, y, 3))

print("=== Prediksi di x=9 ===")
print(f"Derajat 2 : {model_d2(9):.1f}")
print(f"Derajat 3 : {model_d3(9):.1f}")

# Menghitung R-squared — seberapa baik model cocok dengan data
# R² mendekati 1 → model sangat cocok; mendekati 0 → kurang cocok
def r_squared(y_asli, y_prediksi):
    ss_res = np.sum((y_asli - y_prediksi) ** 2)
    ss_tot = np.sum((y_asli - np.mean(y_asli)) ** 2)
    return round(1 - ss_res / ss_tot, 4)

print(f"\nR² derajat 2 : {r_squared(y, model_d2(x))}")
print(f"R² derajat 3 : {r_squared(y, model_d3(x))}")

# Visualisasi data asli + kurva regresi
x_garis = np.linspace(min(x), max(x), 200)

plt.scatter(x, y, color="steelblue", label="Data asli")
plt.plot(x_garis, model_d2(x_garis), color="salmon",  label="Derajat 2")
plt.plot(x_garis, model_d3(x_garis), color="green",   label="Derajat 3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regresi Polinomial Derajat 2 vs 3")
plt.legend()
plt.savefig("plot_regresi_polinomial.png")
plt.clf()
print("\nplot_regresi_polinomial.png disimpan.")

# Bahaya overfitting — derajat terlalu tinggi
plt.scatter(x, y, color="steelblue", label="Data asli")

for derajat in [2, 5, 10]:
    model = np.poly1d(np.polyfit(x, y, derajat))
    r2    = r_squared(y, model(x))
    plt.plot(x_garis, model(x_garis), label=f"Derajat {derajat} (R²={r2})")

plt.ylim(40, 120)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Perbandingan Derajat (Awas Overfitting!)")
plt.legend()
plt.savefig("plot_overfitting.png")
plt.clf()
print("plot_overfitting.png disimpan.")

# Fungsi reusable — prediksi dari model polinomial
def prediksi_polinomial(x_latih, y_latih, x_baru, derajat=2):
    model = np.poly1d(np.polyfit(x_latih, y_latih, derajat))
    return [round(model(xi), 2) for xi in x_baru]

hasil = prediksi_polinomial(x, y, [4, 11, 14], derajat=3)
print(f"\nPrediksi untuk x=[4, 11, 14]: {hasil}")

# 3. RANGKUMAN

# - Regresi polinomial digunakan saat data membentuk kurva, bukan garis lurus.
# - Gunakan np.polyfit(x, y, derajat) dan np.poly1d() untuk membuat model.
# - R² mendekati 1 artinya model sangat cocok dengan data.
# - Derajat terlalu tinggi menyebabkan overfitting — model terlalu mengikuti noise.
# - Pilih derajat paling rendah yang masih memberikan R² yang baik.