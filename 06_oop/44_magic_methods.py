# 1. KONSEP

# Magic method adalah method khusus yang diawali dan diakhiri dua garis bawah.
# Disebut juga "dunder" (double underscore).
#
# Magic method memungkinkan objek bekerja dengan fungsi dan operator bawaan Python.
#
# Yang sering digunakan:
# - __str__  → menentukan tampilan saat print(objek)
# - __repr__ → tampilan untuk debugging (lebih teknis dari __str__)
# - __eq__   → menentukan hasil objek == objek
# - __len__  → menentukan hasil len(objek)
# - __add__  → menentukan hasil objek + objek

# 2. CONTOH

# __str__ dan __repr__
class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Titik({self.x}, {self.y})"   # untuk print()

    def __repr__(self):
        return f"Titik(x={self.x}, y={self.y})"  # untuk debugging

t = Titik(3, 5)
print(t)        # Titik(3, 5)   → pakai __str__
print(repr(t))  # Titik(x=3, y=5) → pakai __repr__

# __eq__ — membandingkan dua objek berdasarkan nilai
class Poin:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, lain):
        return self.x == lain.x and self.y == lain.y

p1 = Poin(1, 2)
p2 = Poin(1, 2)
p3 = Poin(3, 4)

print(p1 == p2)  # True  — nilai sama
print(p1 == p3)  # False — nilai beda

# __len__ — mendukung fungsi len()
class Keranjang:
    def __init__(self):
        self.isi = []

    def tambah(self, item):
        self.isi.append(item)

    def __len__(self):
        return len(self.isi)

    def __str__(self):
        return f"Keranjang: {self.isi}"

k = Keranjang()
k.tambah("apel")
k.tambah("pisang")
k.tambah("mangga")

print(len(k))  # 3
print(k)       # Keranjang: ['apel', 'pisang', 'mangga']

# __add__ dan __sub__ — operasi matematika antar objek
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def __eq__(self, lain):
        return self.x == lain.x and self.y == lain.y

    def __add__(self, lain):
        return Vektor(self.x + lain.x, self.y + lain.y)

    def __sub__(self, lain):
        return Vektor(self.x - lain.x, self.y - lain.y)

v1 = Vektor(1, 2)
v2 = Vektor(3, 4)

print(v1 + v2)   # Vektor(4, 6)
print(v2 - v1)   # Vektor(2, 2)
print(v1 == v2)  # False

# 3. RANGKUMAN

# - Magic method diawali dan diakhiri __ (dunder).
# - __str__  → tampilan saat print() dipanggil.
# - __repr__ → tampilan teknis untuk debugging.
# - __eq__   → mengatur perilaku operator ==.
# - __len__  → mengatur perilaku fungsi len().
# - __add__  → mengatur perilaku operator +.