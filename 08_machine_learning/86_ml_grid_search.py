# 1. KONSEP

# Hyperparameter adalah pengaturan model yang ditentukan sebelum pelatihan.
# Contoh: max_depth pada Decision Tree, C pada SVM.
#
# Grid Search mencoba SEMUA kombinasi hyperparameter yang ditentukan
# dan memilih kombinasi terbaik berdasarkan cross-validation.
#
# Cross-validation (cv=3):
# - Data dibagi menjadi 3 bagian
# - Model dilatih 3 kali, setiap kali menggunakan bagian berbeda sebagai data uji
# - Skor rata-rata dari 3 percobaan digunakan untuk membandingkan kombinasi
#
# Kelemahan: semakin banyak kombinasi → semakin lama waktu komputasi

# 2. CONTOH

from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Data: [usia, punya_pengalaman] → diterima (1) atau tidak (0)
X = [
    [25, 1], [45, 0], [35, 1], [23, 0],
    [50, 1], [40, 0], [32, 1], [28, 0],
]
y = [0, 1, 1, 0, 1, 0, 1, 0]

# Grid hyperparameter yang akan dicoba
param_grid = {
    "max_depth" : [1, 2, 3],
    "criterion" : ["gini", "entropy"],
}

# Total kombinasi: 3 × 2 = 6 kombinasi × cv=3 = 18 kali pelatihan
search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=3
)
search.fit(X, y)

print("=== Hasil Grid Search ===")
print(f"Parameter terbaik : {search.best_params_}")
print(f"Skor terbaik (cv) : {search.best_score_:.4f}")

# Model terbaik langsung siap digunakan
model_terbaik = search.best_estimator_
print(f"\nPrediksi [30, 1]  : {model_terbaik.predict([[30, 1]])[0]}")
print(f"Prediksi [24, 0]  : {model_terbaik.predict([[24, 0]])[0]}")

# Melihat semua hasil kombinasi
print("\n=== Semua Kombinasi yang Dicoba ===")
hasil_grid = pd.DataFrame(search.cv_results_)
kolom = ["param_max_depth", "param_criterion", "mean_test_score"]
print(hasil_grid[kolom].sort_values("mean_test_score", ascending=False).to_string(index=False))

# Menambahkan hyperparameter ketiga
param_grid_luas = {
    "max_depth"       : [1, 2, 3],
    "criterion"       : ["gini", "entropy"],
    "min_samples_split": [2, 3],
}
# Total: 3 × 2 × 2 = 12 kombinasi × cv=3 = 36 kali pelatihan
search_luas = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid_luas,
    cv=3
)
search_luas.fit(X, y)

print("\n=== Grid Search dengan 3 Hyperparameter ===")
print(f"Parameter terbaik : {search_luas.best_params_}")
print(f"Skor terbaik (cv) : {search_luas.best_score_:.4f}")

# Fungsi reusable — tuning dan kembalikan model terbaik
def tuning_model(model, param_grid, X, y, cv=3):
    search = GridSearchCV(model, param_grid, cv=cv)
    search.fit(X, y)
    print(f"Parameter terbaik : {search.best_params_}")
    print(f"Skor terbaik      : {search.best_score_:.4f}")
    return search.best_estimator_

model_hasil = tuning_model(
    DecisionTreeClassifier(random_state=42),
    {"max_depth": [1, 2, 3, 4]},
    X, y
)

# 3. RANGKUMAN

# - Hyperparameter adalah pengaturan model yang ditentukan sebelum pelatihan.
# - Grid Search mencoba semua kombinasi hyperparameter secara otomatis.
# - cross-validation (cv) memastikan hasil evaluasi lebih andal dan tidak bias.
# - search.best_params_ menyimpan kombinasi terbaik yang ditemukan.
# - search.best_estimator_ langsung mengembalikan model terbaik yang siap dipakai.
# - Semakin banyak kombinasi dan nilai cv → semakin akurat tapi semakin lama.