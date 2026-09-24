# 1. KONSEP

# Cross Validation adalah teknik evaluasi model yang lebih andal
# dari satu kali train/test split biasa.
#
# Cara kerja k-fold cross validation:
# 1. Data dibagi menjadi k bagian (fold)
# 2. Model dilatih k kali — setiap kali menggunakan bagian berbeda sebagai data uji
# 3. Skor akhir = rata-rata dari k percobaan
#
# Keunggulan dibanding split biasa:
# - Setiap data pernah menjadi data uji tepat satu kali
# - Hasil evaluasi lebih stabil dan tidak bergantung pada keberuntungan split
# - Std deviation skor menunjukkan seberapa konsisten model

# 2. CONTOH

import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Data acak untuk percobaan
rng = np.random.default_rng(seed=42)
X   = rng.random((30, 2))
y   = rng.integers(0, 2, 30)

# 5-fold cross validation
skor_5 = cross_val_score(
    DecisionTreeClassifier(random_state=42), X, y, cv=5
)

print("=== 5-Fold Cross Validation (Decision Tree) ===")
for i, skor in enumerate(skor_5, start=1):
    print(f"  Fold {i}: {skor:.4f}")
print(f"Rata-rata : {skor_5.mean():.4f}")
print(f"Std Dev   : {skor_5.std():.4f}")
print("(Std kecil → model konsisten di semua fold)")

# 10-fold cross validation — lebih banyak fold, evaluasi lebih detail
skor_10 = cross_val_score(
    DecisionTreeClassifier(random_state=42), X, y, cv=10
)

print("\n=== 10-Fold Cross Validation (Decision Tree) ===")
print(f"Rata-rata : {skor_10.mean():.4f}")
print(f"Std Dev   : {skor_10.std():.4f}")

# Perbandingan beberapa model dengan cross validation
print("\n=== Perbandingan Model ===")
model_daftar = {
    "Decision Tree"      : DecisionTreeClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
}

for nama, model in model_daftar.items():
    skor = cross_val_score(model, X, y, cv=5)
    print(f"{nama:<22} → rata-rata: {skor.mean():.4f}, std: {skor.std():.4f}")

# Mengapa cross validation lebih baik dari satu split?
print("\n=== Mengapa Cross Validation Lebih Andal? ===")
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

skor_split_list = []
for seed in range(10):
    X_latih, X_uji, y_latih, y_uji = train_test_split(
        X, y, test_size=0.3, random_state=seed
    )
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_latih, y_latih)
    skor_split_list.append(accuracy_score(y_uji, model.predict(X_uji)))

print(f"Skor train/test split (10 seed berbeda):")
print(f"  Min: {min(skor_split_list):.4f}, Max: {max(skor_split_list):.4f}")
print(f"  Rentang: {max(skor_split_list)-min(skor_split_list):.4f}")
print(f"Cross validation 5-fold: rata-rata={skor_5.mean():.4f}, std={skor_5.std():.4f}")
print("→ Cross validation lebih stabil, tidak bergantung pada satu split saja.")

# Fungsi reusable — cross validate dan kembalikan mean + std
def evaluasi_cv(model, X, y, fold=5):
    skor = cross_val_score(model, X, y, cv=fold)
    return {
        "fold"     : fold,
        "rata_rata": round(skor.mean(), 4),
        "std"      : round(skor.std(), 4),
    }

hasil = evaluasi_cv(DecisionTreeClassifier(random_state=42), X, y, fold=5)
print("\n=== Hasil Fungsi evaluasi_cv ===")
for k, v in hasil.items():
    print(f"{k:<12}: {v}")

# 3. RANGKUMAN

# - Cross validation melatih dan menguji model k kali pada fold data yang berbeda.
# - Lebih andal dari satu train/test split karena tidak bergantung pada keberuntungan.
# - Gunakan cross_val_score(model, X, y, cv=k) dari sklearn.
# - Rata-rata skor = estimasi performa model; std kecil = model konsisten.
# - Semakin banyak fold → evaluasi lebih detail, tapi waktu komputasi lebih lama.