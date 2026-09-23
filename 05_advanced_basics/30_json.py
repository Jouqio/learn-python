# 1. KONSEP

# JSON (JavaScript Object Notation) adalah format teks untuk menyimpan
# dan bertukar data — umum digunakan di API dan file konfigurasi.
#
# Modul json menyediakan empat fungsi utama:
# - json.dumps() → dict Python ke teks JSON
# - json.loads() → teks JSON ke dict Python
# - json.dump()  → tulis JSON ke file
# - json.load()  → baca JSON dari file

# 2. CONTOH

import json

# dict Python → teks JSON
data = {"nama": "Nadia", "usia": 24, "keahlian": ["Python", "SQL"]}
teks_json = json.dumps(data, indent=2, ensure_ascii=False)
print(teks_json)

# teks JSON → dict Python
hasil = json.loads(teks_json)
print(hasil["nama"])        # Nadia
print(hasil["keahlian"])    # ['Python', 'SQL']

# Menulis JSON ke file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Membaca JSON dari file
with open("data.json", "r", encoding="utf-8") as f:
    dari_file = json.load(f)
print(dari_file)

# Menangani JSON yang tidak valid dengan try/except
teks_rusak = '{"nama": "Andi", "usia": }'  # JSON tidak valid
try:
    json.loads(teks_rusak)
except json.JSONDecodeError as e:
    print(f"Format JSON salah: {e}")

# Contoh nyata: settings manager
import os

FILE_SETTINGS = "settings.json"
DEFAULT_SETTINGS = {"tema": "terang", "bahasa": "id", "notifikasi": True}

def muat_settings():
    if os.path.exists(FILE_SETTINGS):
        with open(FILE_SETTINGS, "r", encoding="utf-8") as f:
            return json.load(f)
    # File belum ada — buat dengan nilai default
    with open(FILE_SETTINGS, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_SETTINGS, f, indent=2, ensure_ascii=False)
    return DEFAULT_SETTINGS

settings = muat_settings()
print(settings)

# 3. RANGKUMAN

# - json.dumps() mengubah dict Python menjadi teks JSON.
# - json.loads() mengubah teks JSON menjadi dict Python.
# - json.dump() dan json.load() digunakan untuk baca/tulis file JSON.
# - Gunakan ensure_ascii=False agar karakter non-Latin (seperti huruf Indonesia) tersimpan dengan benar.
# - Selalu tangani json.JSONDecodeError saat memproses JSON dari luar (API, file).