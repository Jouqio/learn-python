# 1. KONSEP

# Dictionary menyimpan data dalam bentuk pasangan kunci-nilai (key: value).
# Ditulis dengan tanda kurung kurawal: {"kunci": "nilai"}
#
# Sifat dictionary:
# - Kunci harus unik — tidak boleh ada kunci yang sama
# - Nilai bisa berupa tipe data apa saja
# - Berurutan (sejak Python 3.7+)

# 2. CONTOH

# Membuat dictionary
siswa = {"nama": "Bagas", "usia": 22, "jurusan": "Teknik Informatika"}
print(siswa)

# Mengakses nilai lewat kunci
print(siswa["nama"])   # Bagas
print(siswa["usia"])   # 22

# Menggunakan .get() — aman, tidak error jika kunci tidak ada
print(siswa.get("ipk", "belum tersedia"))  # belum tersedia

# Menambah dan mengubah nilai
siswa["ipk"] = 3.7       # tambah kunci baru
siswa["usia"] = 23       # ubah nilai yang sudah ada
print(siswa)

# Menghapus item
del siswa["usia"]
print(siswa)

# Mengecek keberadaan kunci
print("nama" in siswa)    # True
print("usia" in siswa)    # False

# Iterasi dictionary
for kunci, nilai in siswa.items():
    print(f"{kunci}: {nilai}")

# Hanya kunci atau hanya nilai
print(list(siswa.keys()))    # ['nama', 'jurusan', 'ipk']
print(list(siswa.values()))  # ['Bagas', 'Teknik Informatika', 3.7]

# Menggabungkan dua dictionary
ekstra = {"angkatan": 2022, "aktif": True}
siswa.update(ekstra)
print(siswa)

# Contoh nyata: menghitung frekuensi kata
kalimat = "belajar python itu seru dan python itu mudah"
frekuensi = {}

for kata in kalimat.split():
    frekuensi[kata] = frekuensi.get(kata, 0) + 1

print(frekuensi)

# 3. RANGKUMAN

# - Dictionary menyimpan pasangan kunci-nilai: {"kunci": "nilai"}
# - Gunakan .get() untuk mengakses nilai dengan aman (tidak error).
# - Gunakan .update() untuk menggabungkan dua dictionary.
# - Iterasi dengan .items() untuk mengakses kunci dan nilai sekaligus.