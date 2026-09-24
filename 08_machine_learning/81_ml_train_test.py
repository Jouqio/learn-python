# 1. KONSEP

# Sebelum melatih model ML, data harus dibagi menjadi dua bagian:
#
# - Data latih (training set) → digunakan untuk melatih model
# - Data uji (test set)       → digunakan untuk menguji model
#
# Mengapa perlu dipisah?
# - Model yang diuji pada data latihannya sendiri akan terlihat sangat bagus
#   padahal belum tentu bekerja baik pada data baru (overfitting)
# - Test set mensimulasikan "data dunia nyata" yang belum pernah dilihat model
#
# Rasio umum: 80% latih / 20% uji  atau  75% latih / 25% uji

# 2. CONTOH

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

# Dataset sederhana
X = np.arange(20).reshape(-1, 1)   # fitur input
y = np.arange(20) * 2              # target output

# Membagi data — random_state memastikan hasil selalu sama
X_latih, X_uji, y_latih, y_uji = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("=== Hasil Pembagian Data ===")
print(f"Total data  : {len(X)}")
print(f"Data latih  : {len(X_latih)} ({len(X_latih)/len(X)*100:.0f}%)")
print(f"Data uji    : {len(X_uji)} ({len(X_uji)/len(X)*100:.0f}%)")

# Pengaruh ukuran test_size
print("\n=== Pengaruh test_size ===")
for ukuran in [0.1, 0.2, 0.3, 0.4]:
    X_tr, X_te, _, _ = train_test_split(X, y, test_size=ukuran, random_state=42)
    print(f"test_size={ukuran} → latih: {len(X_tr)}, uji: {len(X_te)}")

# Latih model dan evaluasi pada test set
model = linear_model.LinearRegression()
model.fit(X_latih, y_latih)

y_prediksi = model.predict(X_uji)

skor_latih = r2_score(y_latih, model.predict(X_latih))
skor_uji   = r2_score(y_uji, y_prediksi)

print(f"\n=== Evaluasi Model ===")
print(f"R² pada data latih : {skor_latih:.4f}")
print(f"R² pada data uji   : {skor_uji:.4f}")
print("(Jika skor latih >> uji → indikasi overfitting)")

# Fungsi reusable — bagi, latih, dan evaluasi sekaligus
def evaluasi_split(model, X, y, ukuran_uji=0.2):
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=ukuran_uji, random_state=42
    )
    model.fit(X_latih, y_latih)
    skor = r2_score(y_uji, model.predict(X_uji))
    print(f"Ukuran uji: {ukuran_uji*100:.0f}% | R² pada test set: {skor:.4f}")
    return skor

evaluasi_split(linear_model.LinearRegression(), X, y, ukuran_uji=0.2)
evaluasi_split(linear_model.LinearRegression(), X, y, ukuran_uji=0.3)

# 3. RANGKUMAN

# - Selalu pisahkan data menjadi data latih dan data uji sebelum melatih model.
# - Jangan uji model pada data yang sama digunakan untuk melatihnya.
# - Gunakan random_state agar pembagian data bisa direproduksi.
# - R² jauh lebih tinggi pada data latih daripada uji → tanda overfitting.
# - Rasio 80/20 atau 75/25 adalah pilihan umum untuk split data.