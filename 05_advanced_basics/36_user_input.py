# 1. KONSEP

# input() digunakan untuk meminta pengguna mengetik sesuatu.
# Hasil dari input() SELALU berupa string (teks),
# jadi harus dikonversi jika butuh angka.

# 2. CONTOH

# Catatan: kode di bawah ini akan meminta input saat dijalankan.
# Jalankan file ini di terminal, bukan di run biasa jika IDE memblokir input.

# Input dasar
nama = input("Siapa namamu? ")
print(f"Halo, {nama}!")

# Konversi input ke angka
usia = int(input("Berapa umurmu? "))
print(f"Tahun depan kamu berumur {usia + 1} tahun.")

# Konversi ke float
nilai = float(input("Masukkan nilaimu: "))
print(f"Nilaimu adalah {nilai:.1f}")

# Menghitung dua angka dari input pengguna
a = float(input("Angka pertama : "))
b = float(input("Angka kedua   : "))
print(f"Hasil penjumlahan: {a + b}")

# Input dengan validasi — ulangi sampai input valid
while True:
    teks = input("Masukkan angka positif: ")
    try:
        angka = float(teks)
        if angka > 0:
            break
        print("Angka harus lebih dari nol.")
    except ValueError:
        print("Itu bukan angka. Coba lagi.")
print(f"Angka yang kamu masukkan: {angka}")

# Input pilihan ya/tidak
jawaban = input("Lanjutkan? (ya/tidak): ").strip().lower()
if jawaban == "ya":
    print("Melanjutkan program...")
else:
    print("Program dihentikan.")

# Menu sederhana interaktif
print("\n=== MENU ===")
print("1. Hitung luas persegi")
print("2. Hitung keliling lingkaran")

pilihan = input("Pilih menu (1/2): ")

if pilihan == "1":
    sisi = float(input("Masukkan panjang sisi: "))
    print(f"Luas persegi: {sisi ** 2}")
elif pilihan == "2":
    import math
    r = float(input("Masukkan jari-jari: "))
    print(f"Keliling lingkaran: {2 * math.pi * r:.2f}")
else:
    print("Pilihan tidak tersedia.")

# 3. RANGKUMAN

# - input() selalu mengembalikan string — konversi dengan int() atau float() jika perlu.
# - Gunakan .strip() untuk menghapus spasi di awal/akhir input.
# - Gunakan .lower() agar perbandingan tidak sensitif huruf besar/kecil.
# - Selalu validasi input pengguna dengan try/except atau kondisi if.