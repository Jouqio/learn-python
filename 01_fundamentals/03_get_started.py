# 1. KONSEP

# Kode Python bisa dijalankan dengan dua cara:
# - Sebagai file skrip (.py) → jalankan lewat terminal atau tombol Play di VS Code
# - Interaktif lewat REPL → ketik langsung di terminal Python
#
# Baris `if __name__ == "__main__":` artinya:
# "Jalankan fungsi ini hanya jika file ini dijalankan langsung,
#  bukan ketika diimpor dari file lain."

# 2. CONTOH
def main():
    print("Jika kamu melihat pesan ini, Python-mu sudah berjalan dengan benar.")

if __name__ == "__main__":
    main()



# 3. RANGKUMAN

# - Jalankan file Python dengan: python nama_file.py
# - Cek versi Python dengan: python --version
# - Gunakan if __name__ == "__main__": agar kode aman saat diimpor.