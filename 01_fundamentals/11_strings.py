# 1. KONSEP

# String adalah urutan karakter yang diapit tanda kutip.
# String bersifat immutable — nilainya tidak bisa diubah langsung,
# tapi bisa dibuat string baru dari hasilnya.
#
# Yang bisa dilakukan dengan string:
# - Slicing (mengambil sebagian karakter)
# - Method bawaan: .upper(), .lower(), .strip(), .split(), dll.
# - f-string untuk menyisipkan variabel ke dalam teks

# 2. CONTOH

# Membuat string
salam = "  Halo, Pelajar Python!  "

# Method dasar
print(salam.strip())          # hapus spasi di kiri & kanan
print(salam.strip().upper())  # ubah ke huruf besar
print(salam.strip().lower())  # ubah ke huruf kecil

# split() — memecah string menjadi list
print(salam.strip().split(","))  # ['Halo', ' Pelajar Python!']

# len() — menghitung panjang string
nama = "Rafi"
print(len(nama))  # 4

# f-string — menyisipkan variabel ke dalam teks
print(f"Halo, {nama}! Namamu terdiri dari {len(nama)} huruf.")

# Slicing — mengambil sebagian karakter
teks = "Python"
print(teks[0])     # P        (karakter pertama)
print(teks[-1])    # n        (karakter terakhir)
print(teks[0:3])   # Pyt      (indeks 0 sampai 2)
print(teks[::-1])  # nohtyP   (dibalik)

# Method lain yang sering dipakai
kalimat = "belajar python itu menyenangkan"
print(kalimat.count("a"))          # hitung huruf 'a'
print(kalimat.startswith("belajar"))  # True
print(kalimat.endswith("kan"))        # True
print(kalimat.replace("python", "Python"))  # ganti kata

# 3. RANGKUMAN

# - String diapit tanda kutip tunggal atau ganda.
# - Gunakan f-string untuk menyisipkan variabel: f"Halo, {nama}"
# - Slicing mengambil bagian string: teks[awal:akhir]
# - Method seperti .strip(), .upper(), .split() tidak mengubah
#   string asli — mereka menghasilkan string baru.