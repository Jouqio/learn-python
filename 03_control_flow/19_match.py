# 1. KONSEP

# Match statement adalah alternatif yang lebih rapi dari if/elif panjang,
# digunakan saat membandingkan satu nilai dengan banyak kemungkinan.
# Tersedia sejak Python 3.10.
#
# Strukturnya:
# match nilai:
#     case kemungkinan_1:
#         jalankan ini
#     case kemungkinan_2:
#         jalankan ini
#     case _:
#         jalankan ini jika tidak ada yang cocok (default)

# 2. CONTOH


# Match dasar — mengecek kode status HTTP
def cek_status(kode):
    match kode:
        case 200:
            return "OK — permintaan berhasil"
        case 404:
            return "Not Found — halaman tidak ditemukan"
        case 500 | 502 | 503:
            return "Server Error — ada masalah di server"
        case _:
            return "Status tidak dikenal"

print(cek_status(200))  # OK — permintaan berhasil
print(cek_status(404))  # Not Found — halaman tidak ditemukan
print(cek_status(502))  # Server Error — ada masalah di server

# Match dengan string — dispatcher perintah sederhana
def jalankan_perintah(perintah):
    match perintah:
        case "mulai":
            return "Program dimulai."
        case "berhenti":
            return "Program dihentikan."
        case "jeda":
            return "Program dijeda."
        case _:
            return f"Perintah '{perintah}' tidak dikenali."

print(jalankan_perintah("mulai"))    # Program dimulai.
print(jalankan_perintah("jeda"))     # Program dijeda.
print(jalankan_perintah("restart"))  # Perintah 'restart' tidak dikenali.

# Match dengan tuple — mencocokkan pola koordinat
def cek_posisi(titik):
    match titik:
        case (0, 0):
            return "Titik asal (origin)"
        case (0, y):
            return f"Pada sumbu Y di {y}"
        case (x, 0):
            return f"Pada sumbu X di {x}"
        case (x, y):
            return f"Titik biasa di ({x}, {y})"

print(cek_posisi((0, 0)))   # Titik asal (origin)
print(cek_posisi((0, 5)))   # Pada sumbu Y di 5
print(cek_posisi((3, 7)))   # Titik biasa di (3, 7)

# 3. RANGKUMAN

# - match cocok digunakan saat satu nilai dibandingkan dengan banyak kemungkinan.
# - Gunakan | untuk mencocokkan beberapa nilai dalam satu case.
# - case _ adalah default — dijalankan jika tidak ada case yang cocok.
# - match juga bisa mencocokkan pola tuple, bukan hanya nilai tunggal.