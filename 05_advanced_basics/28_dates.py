# 1. KONSEP

# Modul datetime menyediakan alat untuk bekerja dengan tanggal dan waktu.
#
# Yang sering digunakan:
# - datetime.now()     → waktu saat ini
# - timedelta          → selisih atau penambahan waktu
# - strftime()         → mengubah datetime ke format teks
# - strptime()         → mengubah teks ke objek datetime

# 2. CONTOH

from datetime import datetime, timedelta

# Mendapatkan waktu saat ini
sekarang = datetime.now()
print(sekarang)                          # 2026-09-23 14:30:00.123456

# Memformat tanggal ke teks yang lebih rapi
print(sekarang.strftime("%d/%m/%Y"))     # 23/09/2026
print(sekarang.strftime("%Y-%m-%d %H:%M"))  # 2026-09-23 14:30
print(sekarang.strftime("%A"))           # Wednesday (nama hari)

# Mengakses bagian-bagian tanggal
print(sekarang.year)    # 2026
print(sekarang.month)   # 9
print(sekarang.day)     # 23

# timedelta — menambah atau mengurangi waktu
minggu_depan  = sekarang + timedelta(days=7)
kemarin       = sekarang - timedelta(days=1)
print(minggu_depan.strftime("%d/%m/%Y"))  # 7 hari ke depan
print(kemarin.strftime("%d/%m/%Y"))       # kemarin

# Menghitung selisih antara dua tanggal
mulai  = datetime(2026, 1, 1)
akhir  = datetime(2026, 9, 23)
selisih = akhir - mulai
print(f"Selisih: {selisih.days} hari")   # 265 hari

# Mengubah teks ke objek datetime (parsing)
teks_tanggal = "2026-01-15"
tanggal = datetime.strptime(teks_tanggal, "%Y-%m-%d")
print(tanggal)                            # 2026-01-15 00:00:00

# Contoh nyata: menghitung hari sampai ulang tahun
def hari_sampai_ulang_tahun(bulan, tanggal):
    hari_ini    = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    ultah_tahun_ini = hari_ini.replace(month=bulan, day=tanggal)

    if ultah_tahun_ini < hari_ini:
        ultah_tahun_ini = ultah_tahun_ini.replace(year=hari_ini.year + 1)

    return (ultah_tahun_ini - hari_ini).days

print(f"Hari sampai ulang tahun: {hari_sampai_ulang_tahun(12, 25)} hari")

# 3. RANGKUMAN

# - datetime.now() mengambil tanggal dan waktu saat ini.
# - strftime() mengubah datetime ke format teks yang diinginkan.
# - strptime() mengubah teks menjadi objek datetime.
# - timedelta digunakan untuk menambah, mengurangi, atau menghitung selisih waktu.