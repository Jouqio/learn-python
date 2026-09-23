# 1. KONSEP

# Ada tiga jenis method dalam class Python:
#
# - Instance method → pakai self, mengakses data objek
# - Class method    → pakai cls, mengakses data class (decorator @classmethod)
# - Static method   → tidak pakai self atau cls, fungsi biasa di dalam class
#
# Pilih berdasarkan apa yang dibutuhkan:
# - Butuh data objek?   → instance method
# - Butuh data class?   → class method
# - Tidak butuh keduanya? → static method

# 2. CONTOH
class Pizza:
    def __init__(self, ukuran, topping="keju"):
        self.ukuran  = ukuran
        self.topping = topping

    # Instance method — mengakses data objek lewat self
    def info(self):
        return f"Pizza {self.ukuran} dengan {self.topping}"

    # Class method — membuat objek dengan konfigurasi siap pakai
    @classmethod
    def kecil(cls):
        return cls("kecil")

    @classmethod
    def besar_spesial(cls):
        return cls("besar", "pepperoni")

    # Static method — utilitas yang tidak butuh data objek atau class
    @staticmethod
    def ukuran_valid(ukuran):
        return ukuran in ("kecil", "sedang", "besar")

# Memanggil instance method
p1 = Pizza("sedang", "jamur")
print(p1.info())              # Pizza sedang dengan jamur

# Memanggil class method — tanpa membuat objek dulu
p2 = Pizza.kecil()
p3 = Pizza.besar_spesial()
print(p2.info())              # Pizza kecil dengan keju
print(p3.info())              # Pizza besar dengan pepperoni

# Memanggil static method — bisa lewat class atau objek
print(Pizza.ukuran_valid("besar"))   # True
print(Pizza.ukuran_valid("jumbo"))   # False
print(p1.ukuran_valid("kecil"))      # True — bisa dipanggil dari objek juga

# Contoh nyata: class Suhu
class Suhu:
    def __init__(self, celsius):
        self.celsius = celsius

    # Class method — konstruktor alternatif dari Fahrenheit
    @classmethod
    def dari_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    # Class method — konstruktor alternatif dari string
    @classmethod
    def dari_teks(cls, teks):
        # contoh teks: "36.5C"
        return cls(float(teks.replace("C", "")))

    # Static method — utilitas cek beku
    @staticmethod
    def sedang_beku(celsius):
        return celsius <= 0

    def info(self):
        return f"{self.celsius:.1f}°C"

s1 = Suhu(100)
s2 = Suhu.dari_fahrenheit(98.6)
s3 = Suhu.dari_teks("36.5C")

print(s1.info())                    # 100.0°C
print(s2.info())                    # 37.0°C
print(s3.info())                    # 36.5°C
print(Suhu.sedang_beku(-5))        # True
print(Suhu.sedang_beku(25))        # False

# 3. RANGKUMAN

# - Instance method (self) → untuk mengakses atau mengubah data objek.
# - Class method (@classmethod + cls) → untuk membuat objek dengan cara alternatif.
# - Static method (@staticmethod) → untuk fungsi utilitas yang tidak butuh data objek/class.