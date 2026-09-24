# 1. KONSEP

# Decision Tree adalah model ML yang membuat prediksi lewat serangkaian
# pertanyaan ya/tidak berdasarkan nilai fitur.
#
# Cara kerjanya seperti bagan alur:
# "Apakah usia > 40?" → Ya → "Apakah punya pengalaman?" → Tidak → "Tidak diterima"
#
# Keunggulan:
# - Mudah dipahami dan divisualisasikan
# - Tidak butuh feature scaling
#
# Kelemahan:
# - Pohon yang terlalu dalam → overfitting
# - Gunakan max_depth untuk membatasinya

# 2. CONTOH

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Data: [usia, punya_pengalaman] → diterima kerja (1) atau tidak (0)
X = [
    [25, 1], [45, 0], [35, 1], [23, 0], [50, 1],
    [32, 1], [28, 0], [40, 1], [22, 0], [48, 1],
]
y = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]

# Membuat dan melatih model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Prediksi untuk data baru
print("=== Prediksi ===")
print(f"[30, 1] (30 thn, berpengalaman)  : {model.predict([[30, 1]])[0]}")
print(f"[24, 0] (24 thn, belum pengalaman): {model.predict([[24, 0]])[0]}")

# Kepentingan fitur — fitur mana yang paling berpengaruh
print("\n=== Kepentingan Fitur ===")
fitur = ["Usia", "Pengalaman"]
for nama, bobot in zip(fitur, model.feature_importances_):
    print(f"{nama:<15}: {bobot:.4f}")

# Pengaruh max_depth terhadap akurasi
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("\n=== Pengaruh max_depth ===")
for kedalaman in [1, 2, 3, None]:
    m = DecisionTreeClassifier(max_depth=kedalaman, random_state=42)
    m.fit(X_latih, y_latih)
    akurasi_latih = accuracy_score(y_latih, m.predict(X_latih))
    akurasi_uji   = accuracy_score(y_uji, m.predict(X_uji))
    print(f"max_depth={str(kedalaman):<5} → latih: {akurasi_latih:.2f}, uji: {akurasi_uji:.2f}")

print("(max_depth=None → pohon penuh, rentan overfitting)")

# Fungsi reusable — latih dan laporkan akurasi latih vs uji
def evaluasi_decision_tree(X, y, max_depth=None, ukuran_uji=0.3):
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=ukuran_uji, random_state=42
    )
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    model.fit(X_latih, y_latih)

    akurasi_latih = accuracy_score(y_latih, model.predict(X_latih))
    akurasi_uji   = accuracy_score(y_uji, model.predict(X_uji))

    print(f"max_depth={max_depth} → akurasi latih: {akurasi_latih:.2f}, akurasi uji: {akurasi_uji:.2f}")
    return model

evaluasi_decision_tree(X, y, max_depth=2)
evaluasi_decision_tree(X, y, max_depth=None)

# 3. RANGKUMAN

# - Decision Tree membuat prediksi lewat serangkaian pertanyaan ya/tidak.
# - model.feature_importances_ menunjukkan fitur mana yang paling berpengaruh.
# - Pohon tanpa batas kedalaman cenderung overfitting — gunakan max_depth.
# - Akurasi latih >> akurasi uji adalah tanda overfitting.
# - Decision Tree tidak membutuhkan feature scaling seperti algoritma lain.