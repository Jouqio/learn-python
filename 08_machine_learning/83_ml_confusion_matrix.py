# 1. KONSEP

# Confusion matrix merangkum hasil klasifikasi dalam tabel 2x2
# yang menunjukkan berapa banyak prediksi yang benar dan salah.
#
# Struktur confusion matrix (untuk klasifikasi biner):
#
#                  Prediksi: 0    Prediksi: 1
# Aktual: 0    →  TN (benar negatif)  FP (salah positif)
# Aktual: 1    →  FN (salah negatif)  TP (benar positif)
#
# - TP (True Positive)  → prediksi positif, kenyataan positif ✓
# - TN (True Negative)  → prediksi negatif, kenyataan negatif ✓
# - FP (False Positive) → prediksi positif, kenyataan negatif ✗ (alarm palsu)
# - FN (False Negative) → prediksi negatif, kenyataan positif ✗ (terlewat)
#
# Metrik turunan:
# - Akurasi  = (TP + TN) / total
# - Presisi  = TP / (TP + FP)  → dari yang diprediksi positif, berapa yang benar?
# - Recall   = TP / (TP + FN)  → dari yang benar-benar positif, berapa yang terdeteksi?

# 2. CONTOH

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    ConfusionMatrixDisplay,
    classification_report,
)

# Label asli vs prediksi model
y_asli   = [1, 0, 1, 1, 0, 1, 0, 0]
y_prediksi = [1, 0, 0, 1, 0, 1, 1, 0]

# Confusion matrix
matrix = confusion_matrix(y_asli, y_prediksi)
print("=== Confusion Matrix ===")
print(matrix)
print(f"  TN={matrix[0][0]}  FP={matrix[0][1]}")
print(f"  FN={matrix[1][0]}  TP={matrix[1][1]}")

# Metrik evaluasi
akurasi = accuracy_score(y_asli, y_prediksi)
presisi = precision_score(y_asli, y_prediksi)
recall  = recall_score(y_asli, y_prediksi)

print("\n=== Metrik Evaluasi ===")
print(f"Akurasi : {akurasi:.2f}  → {akurasi*100:.0f}% prediksi benar")
print(f"Presisi : {presisi:.2f}  → dari yang diprediksi positif, {presisi*100:.0f}% benar")
print(f"Recall  : {recall:.2f}  → dari yang benar-benar positif, {recall*100:.0f}% terdeteksi")

# Perbedaan FP vs FN dalam konteks nyata
print("\n=== FP vs FN dalam Konteks Nyata ===")
print("Deteksi penyakit:")
print("  FP → pasien sehat dinyatakan sakit (alarm palsu — membuat cemas)")
print("  FN → pasien sakit dinyatakan sehat (berbahaya — penyakit tidak tertangani)")
print("Untuk kasus medis, recall lebih penting dari presisi.")

# Laporan klasifikasi lengkap
print("\n=== Laporan Lengkap ===")
print(classification_report(y_asli, y_prediksi, target_names=["Negatif", "Positif"]))

# Visualisasi confusion matrix
display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=["Negatif", "Positif"])
display.plot()
plt.title("Confusion Matrix")
plt.savefig("plot_confusion_matrix.png")
plt.clf()
print("plot_confusion_matrix.png disimpan.")

# Fungsi ringkasan klasifikasi
def ringkasan_klasifikasi(y_asli, y_prediksi):
    return {
        "akurasi": round(accuracy_score(y_asli, y_prediksi), 4),
        "presisi": round(precision_score(y_asli, y_prediksi), 4),
        "recall" : round(recall_score(y_asli, y_prediksi), 4),
    }

hasil = ringkasan_klasifikasi(y_asli, y_prediksi)
print("\n=== Ringkasan ===")
for metrik, nilai in hasil.items():
    print(f"{metrik:<10}: {nilai}")

# 3. RANGKUMAN

# - Confusion matrix menunjukkan jenis kesalahan model, bukan hanya jumlahnya.
# - TP/TN adalah prediksi benar; FP/FN adalah prediksi salah.
# - Akurasi cocok jika data seimbang; presisi/recall lebih informatif untuk data tidak seimbang.
# - FP = alarm palsu; FN = kasus terlewat — mana yang lebih berbahaya tergantung konteks.
# - Gunakan classification_report() untuk melihat semua metrik sekaligus.