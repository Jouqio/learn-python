# ============================================
# Topik : Modul (Modules)
# Level : Pemula
# ============================================


# ============================================
# 1. KONSEP
# ============================================
# Modul adalah file .py yang berisi kode yang bisa diimpor dan digunakan
# di file lain. Python sudah menyediakan banyak modul bawaan (standard library)
# yang siap pakai tanpa perlu instalasi tambahan.
#
# Cara mengimpor modul:
# - import modul              → impor seluruh modul
# - from modul import fungsi  → impor fungsi tertentu saja
# - import modul as alias     → impor dengan nama singkat

# 2. CONTOH

# import biasa — akses fungsi lewat nama modul
import math
import random

print(math.pi)            # 3.141592653589793
print(math.sqrt(16))      # 4.0
print(math.floor(3.9))    # 3
print(math.ceil(3.1))     # 4

# random — menghasilkan nilai acak
print(random.randint(1, 6))          # angka acak antara 1-6 (seperti dadu)
print(random.choice(["batu", "gunting", "kertas"]))  # pilih acak dari list

# from ... import — impor fungsi tertentu saja (tanpa awalan modul)
from math import sqrt, pi

print(sqrt(25))   # 5.0  (tidak perlu math.sqrt)
print(pi)         # 3.141592653589793

# import dengan alias — berguna saat nama modul panjang
import random as rnd

print(rnd.randint(1, 100))

# Beberapa modul bawaan yang sering dipakai
import os
import datetime

print(os.getcwd())                          # direktori kerja saat ini
print(datetime.date.today())                # tanggal hari ini
print(datetime.datetime.now())              # tanggal dan waktu sekarang

# 3. RANGKUMAN

# - Modul adalah file .py berisi fungsi/variabel yang bisa diimpor ulang.
# - Gunakan import untuk mengimpor seluruh modul.
# - Gunakan from ... import untuk mengimpor fungsi tertentu saja.
# - Gunakan import ... as untuk membuat alias nama modul.
# - Python punya banyak modul bawaan: math, random, os, datetime, dll.