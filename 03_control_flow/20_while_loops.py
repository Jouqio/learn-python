# 1. KONSEP

# While loop mengulangi sebuah blok kode selama kondisinya True.
# Berbeda dengan for loop, while digunakan saat jumlah
# perulangan tidak diketahui sejak awal.
#
# Kata kunci tambahan:
# - break    → keluar dari loop sebelum kondisi selesai
# - continue → lewati iterasi ini, langsung ke iterasi berikutnya

# 2. CONTOH

# While dasar — cetak angka 1 sampai 5
hitung = 1
while hitung <= 5:
    print(f"hitung = {hitung}")
    hitung += 1  # wajib diubah agar tidak infinite loop

# break — keluar dari loop saat kondisi tertentu terpenuhi
n = 10
while n > 0:
    if n == 5:
        break   # berhenti saat n bernilai 5
    n -= 1
print(f"Loop berhenti di n = {n}")  # 5

# continue — lewati iterasi tertentu, lanjut ke berikutnya
angka = 0
while angka < 10:
    angka += 1
    if angka % 3 == 0:
        continue  # lewati kelipatan 3
    print(angka)  # cetak semua kecuali 3, 6, 9

# Mengurangi nilai terus sampai batas tertentu
nilai = 100
while nilai > 1:
    nilai /= 2  # dibagi 2 setiap iterasi
print(f"Nilai akhir: {round(nilai, 4)}")

# Contoh nyata: simulasi hitung mundur
hitungan = 5
while hitungan > 0:
    print(f"Mulai dalam {hitungan}...")
    hitungan -= 1
print("Mulai!")

# while True — loop tanpa batas, dihentikan manual dengan break
percobaan = 3
tebakan   = 7   # anggap ini input pengguna
jawaban   = 7

while True:
    if tebakan == jawaban:
        print("Tebakan benar!")
        break
    percobaan -= 1
    if percobaan == 0:
        print("Kesempatan habis.")
        break

# 3. RANGKUMAN

# - while mengulang kode selama kondisinya True.
# - Pastikan ada perubahan nilai agar tidak terjadi infinite loop.
# - break menghentikan loop lebih awal.
# - continue melewati iterasi saat ini dan lanjut ke berikutnya.
# - while True digunakan saat loop harus jalan terus sampai kondisi break terpenuhi.