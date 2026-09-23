# 1. KONSEP

# print() digunakan untuk menampilkan teks atau nilai ke layar (konsol).
#
# Parameter tambahan yang berguna:
# - sep  → pemisah antar argumen (default: spasi)
# - end  → karakter di akhir output (default: baris baru)

# 2. CONTOH

# print() biasa
print("Halo, Python!")

# Beberapa argumen sekaligus
print("Python", "itu", "menyenangkan")

# Mengubah pemisah dengan sep
print("Python", "itu", "menyenangkan", sep="-")

# Menghapus baris baru dengan end
print("Baris pertama...", end=" ")
print("...sambung di baris yang sama.")

# Mencetak beberapa baris sekaligus dengan triple quotes
print("""Baris satu
Baris dua
Baris tiga""")

# 3. RANGKUMAN

# - print() menampilkan output ke konsol.
# - sep mengatur pemisah antar argumen (default: spasi).
# - end mengatur karakter setelah output (default: baris baru).