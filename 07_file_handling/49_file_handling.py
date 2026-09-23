# 1. KONSEP

# Python bisa membaca dan menulis file menggunakan fungsi open().
#
# Mode yang tersedia:
# - "r"  → baca file (default) — error jika file tidak ada
# - "w"  → tulis file — membuat baru atau menimpa yang sudah ada
# - "a"  → tambah di akhir file tanpa menghapus isi lama
# - "x"  → buat file baru — error jika file sudah ada
#
# Selalu gunakan blok "with" agar file otomatis ditutup
# setelah selesai, bahkan jika terjadi error.

# 2. CONTOH

# Menulis file — mode "w"
with open("contoh.txt", "w", encoding="utf-8") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

# Membaca seluruh isi file — mode "r"
with open("contoh.txt", "r", encoding="utf-8") as f:
    isi = f.read()
print(isi)

# Membaca baris per baris
with open("contoh.txt", "r", encoding="utf-8") as f:
    for baris in f:
        print(baris.strip())  # strip() menghapus \n di akhir baris

# Membaca semua baris sebagai list
with open("contoh.txt", "r", encoding="utf-8") as f:
    semua_baris = f.readlines()
print(semua_baris)  # ['Baris pertama\n', 'Baris kedua\n']

# Menambah isi file — mode "a" (tidak menghapus isi lama)
with open("contoh.txt", "a", encoding="utf-8") as f:
    f.write("Baris ketiga\n")

# Membaca ulang setelah ditambah
with open("contoh.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Menangani file yang tidak ada
try:
    with open("tidak_ada.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File tidak ditemukan.")

# Contoh nyata: menghitung jumlah kata dalam file
def hitung_kata(nama_file):
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            isi = f.read()
        return len(isi.split())
    except FileNotFoundError:
        return 0

print(f"Jumlah kata: {hitung_kata('contoh.txt')}")

# 3. RANGKUMAN

# - Gunakan open() dengan mode yang sesuai: "r", "w", "a", atau "x".
# - Selalu gunakan "with open(...) as f:" agar file otomatis ditutup.
# - Gunakan encoding="utf-8" agar karakter Indonesia terbaca dengan benar.
# - Tangani FileNotFoundError saat membaca file yang mungkin tidak ada.