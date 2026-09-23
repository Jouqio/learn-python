# 1. KONSEP

# Ada beberapa cara membaca file di Python:
#
# - .read()      → membaca seluruh isi file sekaligus sebagai satu string
# - .readline()  → membaca satu baris saja
# - .readlines() → membaca semua baris, hasilnya list
# - for loop     → membaca baris per baris (paling hemat memori)
#
# Pilih cara yang sesuai dengan kebutuhan dan ukuran file.

# 2. CONTOH

# Buat file contoh dulu
with open("contoh.txt", "w", encoding="utf-8") as f:
    f.write("Satu\nDua\nTiga\nEmpat\nLima\n")

# .read() — membaca seluruh isi sekaligus
with open("contoh.txt", "r", encoding="utf-8") as f:
    semua = f.read()
print(semua)

# .readline() — membaca satu baris saja
with open("contoh.txt", "r", encoding="utf-8") as f:
    baris_pertama = f.readline()
    baris_kedua   = f.readline()
print(baris_pertama.strip())  # Satu
print(baris_kedua.strip())    # Dua

# .readlines() — semua baris disimpan dalam list
with open("contoh.txt", "r", encoding="utf-8") as f:
    daftar_baris = f.readlines()
print(daftar_baris)  # ['Satu\n', 'Dua\n', 'Tiga\n', ...]

# for loop — membaca baris per baris (direkomendasikan untuk file besar)
with open("contoh.txt", "r", encoding="utf-8") as f:
    for nomor, baris in enumerate(f, start=1):
        print(f"{nomor}: {baris.strip()}")

# Menghitung jumlah baris dalam file
with open("contoh.txt", "r", encoding="utf-8") as f:
    jumlah_baris = sum(1 for _ in f)
print(f"Jumlah baris: {jumlah_baris}")

# Contoh nyata: membaca file CSV sederhana
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Andi,90,Lulus\n")
    f.write("Budi,55,Tidak Lulus\n")
    f.write("Citra,78,Lulus\n")

def baca_csv_sederhana(nama_file):
    hasil = []
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                kolom = baris.strip().split(",")
                hasil.append(kolom)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    return hasil

data = baca_csv_sederhana("data.txt")
for baris in data:
    print(baris)  # ['Andi', '90', 'Lulus']

# 3. RANGKUMAN

# - .read()      → cocok untuk file kecil yang ingin dibaca sekaligus.
# - .readline()  → cocok saat hanya butuh satu baris tertentu.
# - .readlines() → cocok saat semua baris perlu disimpan dalam list.
# - for loop     → cara terbaik untuk file besar, hemat memori.