# 1. KONSEP

# Exception adalah error yang terjadi saat program berjalan.
# Tanpa penanganan, program akan langsung berhenti (crash).
#
# Struktur penanganan error:
# try     → kode yang mungkin menyebabkan error
# except  → jalankan ini jika error terjadi
# else    → jalankan ini jika TIDAK ada error
# finally → selalu dijalankan, ada error atau tidak

# 2. CONTOH

# try / except dasar
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")

# Menangkap beberapa jenis error sekaligus
def konversi_angka(teks):
    try:
        angka = int(teks)
        hasil = 100 / angka
    except ValueError:
        print(f"'{teks}' bukan angka yang valid.")
        return None
    except ZeroDivisionError:
        print("Angka tidak boleh nol.")
        return None
    else:
        print("Konversi berhasil.")
        return hasil
    finally:
        print("Proses selesai.")  # selalu dijalankan

print(konversi_angka("5"))    # berhasil
print(konversi_angka("abc"))  # ValueError
print(konversi_angka("0"))    # ZeroDivisionError

# Menangkap beberapa error dalam satu baris
try:
    data = [1, 2, 3]
    print(data[10])
except (IndexError, KeyError) as e:
    print(f"Error akses data: {e}")

# raise — memunculkan error secara manual
def cek_usia(usia):
    if not isinstance(usia, int):
        raise ValueError("Usia harus berupa angka bulat.")
    if usia < 0:
        raise ValueError("Usia tidak boleh negatif.")
    return f"Usia valid: {usia} tahun"

try:
    print(cek_usia(20))
    print(cek_usia(-5))
except ValueError as e:
    print(f"Error: {e}")

# Custom exception — membuat jenis error sendiri
class ErrorUsiaTidakValid(Exception):
    pass

def parse_usia(teks):
    try:
        usia = int(teks)
    except ValueError:
        raise ErrorUsiaTidakValid(f"'{teks}' bukan angka.")
    if usia < 0:
        raise ErrorUsiaTidakValid("Usia tidak boleh negatif.")
    return usia

try:
    print(parse_usia("abc"))
except ErrorUsiaTidakValid as e:
    print(f"Usia tidak valid: {e}")

# 3. RANGKUMAN

# - Gunakan try/except agar program tidak crash saat terjadi error.
# - Tangkap error yang spesifik (ZeroDivisionError, ValueError, dll),
#   hindari except tanpa jenis error — terlalu luas dan menyembunyikan bug.
# - else dijalankan jika tidak ada error, finally selalu dijalankan.
# - Gunakan raise untuk memunculkan error secara manual.
# - Buat custom exception dengan mewarisi kelas Exception.