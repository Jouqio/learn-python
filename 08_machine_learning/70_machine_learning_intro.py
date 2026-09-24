# 1. KONSEP

# Machine Learning (ML) adalah cabang kecerdasan buatan di mana
# komputer belajar menemukan pola dari data — tanpa harus diprogram
# secara manual aturan per aturan.
#
# Tiga jenis utama Machine Learning:
#
# 1. Supervised Learning (Pembelajaran Terawasi)
#    → Model dilatih dengan data berlabel (input + jawaban benar)
#    → Contoh: prediksi harga rumah, deteksi spam
#
# 2. Unsupervised Learning (Pembelajaran Tidak Terawasi)
#    → Model mencari pola sendiri dari data tanpa label
#    → Contoh: pengelompokan pelanggan, deteksi anomali
#
# 3. Reinforcement Learning (Pembelajaran Penguatan)
#    → Model belajar dari trial-and-error lewat sistem hadiah/hukuman
#    → Contoh: AI bermain game, robot otonom
#
# Di roadmap ini fokus pada supervised dan unsupervised menggunakan scikit-learn.

# 2. CONTOH


print("=== Pengenalan Machine Learning ===")
print()

print("Jenis-jenis Machine Learning:")
print("1. Supervised   → belajar dari data berlabel")
print("2. Unsupervised → mencari pola tanpa label")
print("3. Reinforcement → belajar dari hadiah dan hukuman")
print()

# Perbedaan model ML vs fungsi biasa
print("Fungsi biasa:")
print("  → Aturan ditulis manual oleh programmer")
print("  → Contoh: if suhu > 30 maka 'panas'")
print()
print("Model Machine Learning:")
print("  → Aturan dipelajari sendiri dari data")
print("  → Contoh: model belajar sendiri apa artinya 'panas' dari ribuan data suhu")
print()

# Pentingnya data
print("Mengapa kualitas data lebih penting dari algoritma:")
print("  → Data kotor menghasilkan prediksi yang salah (garbage in, garbage out)")
print("  → Algoritma terbaik pun tidak bisa memperbaiki data yang buruk")
print("  → Data yang baik + algoritma sederhana sering mengalahkan")
print("    data buruk + algoritma canggih")
print()

# Training data vs test data
print("Training data → data yang digunakan untuk melatih model")
print("Test data     → data baru yang digunakan untuk menguji seberapa baik model bekerja")
print("  → Model tidak boleh 'melihat' test data saat pelatihan")

# 3. RANGKUMAN

# - ML memungkinkan komputer belajar pola dari data tanpa diprogram manual.
# - Supervised: belajar dari data berlabel (ada jawaban benarnya).
# - Unsupervised: mencari pola sendiri tanpa label.
# - Kualitas data lebih menentukan hasil daripada pilihan algoritma.
# - Training data untuk melatih model, test data untuk menguji kinerjanya.