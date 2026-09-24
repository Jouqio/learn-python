# 1. KONSEP

# ROC Curve adalah grafik yang menunjukkan kemampuan model klasifikasi
# dalam membedakan kelas positif dan negatif di berbagai ambang batas keputusan.
#
# Dua sumbu ROC Curve:
# - Sumbu Y → TPR (True Positive Rate / Recall) = TP / (TP + FN)
# - Sumbu X → FPR (False Positive Rate)         = FP / (FP + TN)
#
# AUC (Area Under Curve) — luas di bawah kurva ROC:
# - AUC = 1.0 → model sempurna (memisahkan kedua kelas dengan sempurna)
# - AUC = 0.5 → model acak (tidak lebih baik dari tebakan)
# - AUC < 0.5 → model lebih buruk dari tebakan
#
# Keunggulan AUC: tidak terpengaruh ambang batas keputusan
# dan tetap informatif meski data tidak seimbang.

# 2. CONTOH

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import (
    roc_auc_score,
    roc_curve,
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Label asli dan probabilitas prediksi model
y_asli  = [0, 0, 1, 1, 0, 1, 1, 0]
y_skor  = [0.1, 0.4, 0.35, 0.8, 0.2, 0.7, 0.65, 0.3]

auc = roc_auc_score(y_asli, y_skor)
print(f"=== AUC Score ===")
print(f"AUC : {auc:.3f}")
print(f"Interpretasi: {'Baik (>0.7)' if auc > 0.7 else 'Perlu ditingkatkan'}")

# Arti nilai AUC
print("\n=== Interpretasi Nilai AUC ===")
print("AUC = 1.0 → model sempurna, memisahkan kelas dengan sempurna")
print("AUC = 0.9 → model sangat baik")
print("AUC = 0.7 → model cukup baik")
print("AUC = 0.5 → model acak, tidak lebih baik dari tebakan")
print("AUC < 0.5 → model lebih buruk dari tebakan")

# Plot ROC Curve
fpr, tpr, ambang = roc_curve(y_asli, y_skor)

plt.plot(fpr, tpr, color="steelblue", label=f"ROC Curve (AUC = {auc:.3f})")
plt.plot([0, 1], [0, 1], color="gray", linestyle="--", label="Model acak (AUC = 0.5)")
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.title("ROC Curve")
plt.legend()
plt.savefig("plot_roc_curve.png")
plt.clf()
print("\nplot_roc_curve.png disimpan.")

# Perbandingan AUC dua model pada data yang sama
rng = np.random.default_rng(seed=42)
X   = rng.random((100, 2))
y   = rng.integers(0, 2, 100)

X_latih, X_uji, y_latih, y_uji = train_test_split(X, y, test_size=0.3, random_state=42)

model_lr = LogisticRegression()
model_dt = DecisionTreeClassifier(random_state=42)

model_lr.fit(X_latih, y_latih)
model_dt.fit(X_latih, y_latih)

skor_lr = model_lr.predict_proba(X_uji)[:, 1]
skor_dt = model_dt.predict_proba(X_uji)[:, 1]

auc_lr = roc_auc_score(y_uji, skor_lr)
auc_dt = roc_auc_score(y_uji, skor_dt)

print(f"\n=== Perbandingan AUC Dua Model ===")
print(f"Logistic Regression : AUC = {auc_lr:.4f}")
print(f"Decision Tree       : AUC = {auc_dt:.4f}")
print(f"Model terbaik       : {'Logistic Regression' if auc_lr > auc_dt else 'Decision Tree'}")

# Plot ROC Curve dua model sekaligus
fpr_lr, tpr_lr, _ = roc_curve(y_uji, skor_lr)
fpr_dt, tpr_dt, _ = roc_curve(y_uji, skor_dt)

plt.plot(fpr_lr, tpr_lr, label=f"Logistic Regression (AUC={auc_lr:.3f})")
plt.plot(fpr_dt, tpr_dt, label=f"Decision Tree (AUC={auc_dt:.3f})")
plt.plot([0, 1], [0, 1], "k--", label="Model acak")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Perbandingan ROC Curve Dua Model")
plt.legend()
plt.savefig("plot_roc_perbandingan.png")
plt.clf()
print("plot_roc_perbandingan.png disimpan.")

# Fungsi reusable — bandingkan AUC beberapa model
def bandingkan_auc(daftar_model, X_uji, y_uji):
    hasil = {}
    for nama, model in daftar_model.items():
        skor = model.predict_proba(X_uji)[:, 1]
        hasil[nama] = round(roc_auc_score(y_uji, skor), 4)
    return hasil

model_dict = {
    "Logistic Regression": model_lr,
    "Decision Tree"      : model_dt,
}
auc_dict = bandingkan_auc(model_dict, X_uji, y_uji)

print("\n=== Hasil Fungsi bandingkan_auc ===")
for nama, auc in sorted(auc_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{nama:<22}: {auc}")

# 3. RANGKUMAN

# - ROC Curve memplot TPR vs FPR di berbagai ambang batas keputusan.
# - AUC merangkum kualitas model menjadi satu angka (0.5 hingga 1.0).
# - AUC berguna untuk data tidak seimbang — tidak terpengaruh ambang batas.
# - Gunakan roc_auc_score() untuk menghitung AUC, roc_curve() untuk plotnya.
# - Bandingkan AUC beberapa model untuk memilih yang terbaik secara objektif.