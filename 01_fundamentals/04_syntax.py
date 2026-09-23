# 1. KONSEP

# Python menggunakan indentasi (spasi) untuk menentukan blok kode,
# bukan kurung kurawal seperti bahasa lain.
#
# Aturan indentasi Python:
# - Gunakan 4 spasi (bukan tab)
# - Indentasi yang tidak konsisten akan menyebabkan error

# 2. CONTOH
# Blok if — baris dalam blok harus diindentasi
if True:
    print("Baris ini ada DI DALAM blok if (diindentasi).")
print("Baris ini ada DI LUAR blok if (tidak diindentasi).")

# Contoh nested (blok bersarang)
nilai = 85

if nilai >= 70:
    print("Kamu lulus.")
    if nilai >= 90:
        print("Luar biasa, nilaimu sangat tinggi!")

# 3. RANGKUMAN

# - Indentasi di Python bukan sekadar gaya — ini adalah aturan wajib.
# - Gunakan 4 spasi untuk setiap level blok kode.
# - Indentasi yang salah akan langsung menghasilkan error saat dijalankan.