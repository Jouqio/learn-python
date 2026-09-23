# 1. KONSEP

# None adalah nilai khusus di Python yang berarti "tidak ada nilai".
# Berbeda dari 0, False, atau string kosong "" — None benar-benar kosong.
#
# Aturan penting:
# - Gunakan "is None" untuk mengecek None, bukan "== None"
# - Fungsi yang tidak punya return otomatis mengembalikan None

# 2. CONTOH

# None sebagai penanda "tidak ditemukan"
def cari_pengguna(id_cari, daftar):
    for pengguna in daftar:
        if pengguna["id"] == id_cari:
            return pengguna
    return None  # kembalikan None jika tidak ditemukan

data = [{"id": 1, "nama": "Eka"}, {"id": 2, "nama": "Budi"}]

hasil = cari_pengguna(2, data)
if hasil is not None:
    print(f"Ditemukan: {hasil['nama']}")  # Ditemukan: Budi

tidak_ada = cari_pengguna(99, data)
if tidak_ada is None:
    print("Pengguna tidak ditemukan.")

# Fungsi tanpa return → otomatis None
def cetak_saja(teks):
    print(teks)

nilai_kembali = cetak_saja("Halo")
print(nilai_kembali)   # None

# None sebagai nilai default parameter
def buat_profil(nama, kota=None):
    if kota is None:
        kota = "Tidak diketahui"
    return f"{nama} dari {kota}"

print(buat_profil("Andi"))             # Andi dari Tidak diketahui
print(buat_profil("Andi", "Bontang")) # Andi dari Bontang

# Menyaring None dari list
data_mentah = [1, None, 3, None, 5]
bersih = [x for x in data_mentah if x is not None]
print(bersih)   # [1, 3, 5]

# Mencari angka positif pertama, atau None jika tidak ada
def pertama_positif(angka):
    for n in angka:
        if n > 0:
            return n
    return None

print(pertama_positif([-3, -1, 4, 7]))  # 4
print(pertama_positif([-3, -1, -2]))    # None

# 3. RANGKUMAN

# - None berarti "tidak ada nilai" — bukan 0, bukan False, bukan "".
# - Fungsi tanpa return otomatis mengembalikan None.
# - Gunakan "is None" atau "is not None" untuk mengecek None.
# - None berguna sebagai nilai default parameter yang bisa diganti di dalam fungsi.