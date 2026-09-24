# 1. KONSEP

# Bagging adalah teknik ensemble — menggabungkan banyak model
# yang dilatih pada subset data yang berbeda-beda, lalu
# mengambil hasil prediksi mayoritas (voting).
#
# Cara kerjanya:
# 1. Ambil subset data secara acak (dengan pengulangan/bootstrap)
# 2. Latih satu model pada setiap subset
# 3. Prediksi akhir = hasil voting dari semua model
#
# Keunggulan dibanding satu Decision Tree:
# - Mengurangi overfitting (varians lebih rendah)
# - Lebih stabil — satu data aneh tidak merusak seluruh prediksi
#
# Random Forest = Bagging + pemilihan fitur acak (versi lebih canggih)

# 2. CONTOH

from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

# Data: [usia, punya_pengalaman] → diterima (1) atau tidak (0)
X = [
    [25, 1], [45, 0], [35, 1], [23, 0],
    [50, 1], [40, 0], [60, 1], [22, 0],
]
y = [0, 1, 1, 0, 1, 0, 1, 0]

# Satu Decision Tree (model tunggal)
pohon_tunggal = DecisionTreeClassifier(random_state=42)
pohon_tunggal.fit(X, y)

# BaggingClassifier — banyak pohon, tiap pohon dilatih pada subset berbeda
bagging = BaggingClassifier(
    DecisionTreeClassifier(),
    n_estimators=10,
    random_state=42
)
bagging.fit(X, y)

# Perbandingan prediksi
data_uji = [[30, 1], [24, 0], [55, 1]]
print("=== Perbandingan Prediksi ===")
print(f"{'Data':<12} {'Pohon Tunggal':<18} {'Bagging (10 pohon)'}")
for d in data_uji:
    pred_pohon   = pohon_tunggal.predict([d])[0]
    pred_bagging = bagging.predict([d])[0]
    print(f"{str(d):<12} {pred_pohon:<18} {pred_bagging}")

# Pengaruh jumlah estimator
print("\n=== Pengaruh n_estimators ===")
for n in [1, 5, 10, 20, 50]:
    m = BaggingClassifier(DecisionTreeClassifier(), n_estimators=n, random_state=42)
    skor = cross_val_score(m, X, y, cv=3).mean()
    print(f"n_estimators={n:<4} → skor cv rata-rata: {skor:.4f}")

# Random Forest — bagging + pemilihan fitur acak
rf = RandomForestClassifier(n_estimators=10, random_state=42)
rf.fit(X, y)

print("\n=== Random Forest vs Bagging ===")
for d in data_uji:
    pred_bag = bagging.predict([d])[0]
    pred_rf  = rf.predict([d])[0]
    print(f"{str(d):<12} Bagging: {pred_bag}  Random Forest: {pred_rf}")

# Kepentingan fitur di Random Forest
print("\n=== Kepentingan Fitur (Random Forest) ===")
for nama, bobot in zip(["Usia", "Pengalaman"], rf.feature_importances_):
    print(f"{nama:<15}: {bobot:.4f}")

# Fungsi reusable — bandingkan akurasi pohon tunggal vs bagging
def bandingkan_model(X, y, n_estimators=10, cv=3):
    skor_pohon   = cross_val_score(
        DecisionTreeClassifier(random_state=42), X, y, cv=cv
    ).mean()
    skor_bagging = cross_val_score(
        BaggingClassifier(DecisionTreeClassifier(), n_estimators=n_estimators, random_state=42),
        X, y, cv=cv
    ).mean()

    print(f"Skor pohon tunggal : {skor_pohon:.4f}")
    print(f"Skor bagging       : {skor_bagging:.4f}")
    print(f"Selisih            : {skor_bagging - skor_pohon:+.4f}")

bandingkan_model(X, y)

# 3. RANGKUMAN

# - Bagging melatih banyak model pada subset data berbeda, lalu menggabungkan hasilnya.
# - Lebih stabil dari satu Decision Tree — varians lebih rendah, kurang overfit.
# - Tambah n_estimators untuk hasil lebih stabil (tapi komputasi lebih lama).
# - Random Forest adalah versi bagging yang lebih canggih dengan pemilihan fitur acak.
# - Gunakan cross_val_score() untuk membandingkan model secara adil.