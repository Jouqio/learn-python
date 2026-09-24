# 1. KONSEP

# Django adalah web framework Python yang lengkap — tersedia ORM, admin panel,
# autentikasi, dan banyak lagi tanpa perlu instalasi tambahan.
#
# Django menggunakan pola MVT (Model-View-Template):
# - Model    → mendefinisikan struktur data dan berinteraksi dengan database
# - View     → logika pemrosesan request dan pengiriman response
# - Template → tampilan HTML yang dikirim ke browser
#
# Alur request Django:
# URL → View → (Model jika perlu data) → Template → Response

# 2. CONTOH

# Semua perintah di bawah dijalankan di TERMINAL

# -- SETUP PROJECT BARU --
# pip install django                          → instal Django
# django-admin startproject namaproject      → buat project baru
# cd namaproject
# python manage.py startapp namaapp          → buat app di dalam project

# -- MENJALANKAN SERVER --
# python manage.py runserver                 → jalankan server di localhost:8000

# -- DATABASE --
# python manage.py makemigrations            → buat file migrasi dari model
# python manage.py migrate                   → terapkan migrasi ke database

# -- ADMIN --
# python manage.py createsuperuser           → buat akun admin

print("Perintah utama Django:")
print("  django-admin startproject namaproject")
print("  python manage.py startapp namaapp")
print("  python manage.py runserver")
print("  python manage.py makemigrations && python manage.py migrate")

# Contoh minimal — view function
# (kode ini berada di dalam file views.py, bukan di sini)
contoh_view = """
# views.py
from django.http import HttpResponse

def beranda(request):
    return HttpResponse("Halo dari Django!")
"""

# Contoh minimal — routing URL
# (kode ini berada di dalam file urls.py)
contoh_urls = """
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
]
"""

# Contoh model Django
# (kode ini berada di dalam file models.py)
contoh_model = """
# models.py
from django.db import models

class Post(models.Model):
    judul      = models.CharField(max_length=200)
    isi        = models.TextField()
    dibuat_pada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
"""

print("\nContoh view:")
print(contoh_view)
print("Contoh URL routing:")
print(contoh_urls)
print("Contoh model:")
print(contoh_model)

# 3. RANGKUMAN

# - Django adalah web framework Python yang lengkap — siap pakai tanpa banyak konfigurasi.
# - Pola MVT: Model (data), View (logika), Template (tampilan).
# - Alur: URL diterima → View dijalankan → data dari Model → Template di-render → Response.
# - manage.py adalah alat utama untuk mengelola project Django.
# - Django menyediakan admin panel bawaan yang bisa langsung digunakan.