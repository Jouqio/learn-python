# 1. KONSEP

# Komentar adalah teks yang diabaikan oleh Python saat kode dijalankan.
# Gunakan komentar untuk menjelaskan MENGAPA, bukan mengulang apa yang sudah jelas dari kode.
#
# Cara menulis komentar:
# - Satu baris  → gunakan tanda #
# - Banyak baris → gunakan beberapa baris # berturut-turut

# 2. CONTOH

# Tarif pajak Indonesia (PPN 11%) — nilai ini ditetapkan pemerintah
TARIF_PAJAK = 0.11

harga = 100
total = harga + harga * TARIF_PAJAK
print(total)  # Output: 111.0

# Komentar banyak baris:
# Program ini menghitung total harga setelah pajak.
# Tarif pajak bisa berubah, jadi disimpan sebagai konstanta
# agar mudah diubah di satu tempat saja.

# Baris ini dinonaktifkan sementara (di-comment):
# print("Baris ini tidak akan dijalankan")

# 3. RANGKUMAN

# - Komentar ditulis dengan tanda # di awal baris.
# - Komentar yang baik menjelaskan alasan, bukan mengulang kode.
# - Komentar yang tidak perlu justru membuat kode lebih sulit dibaca.