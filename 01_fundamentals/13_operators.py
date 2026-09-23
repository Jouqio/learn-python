# 1. KONSEP

# Operator adalah simbol untuk melakukan operasi pada nilai atau variabel.
#
# Jenis-jenis operator di Python:
# - Aritmatika   → +, -, *, /, //, %, **
# - Perbandingan → ==, !=, >, <, >=, <=
# - Logika       → and, or, not
# - Penugasan    → =, +=, -=, *=, /=
# - Keanggotaan  → in, not in
# - Identitas    → is, is not

# 2. CONTOH

a, b = 10, 3

# Operator aritmatika
print(a + b)   # penjumlahan        → 13
print(a - b)   # pengurangan        → 7
print(a * b)   # perkalian          → 30
print(a / b)   # pembagian          → 3.333...
print(a // b)  # pembagian bulat    → 3
print(a % b)   # sisa bagi          → 1
print(a ** b)  # pangkat            → 1000

# Operator perbandingan (hasilnya selalu True atau False)
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True

# Operator penugasan
total = 0
total += 10  # sama dengan: total = total + 10
total *= 2   # sama dengan: total = total * 2
print(total) # 20

# Operator keanggotaan
print(5 in [1, 5, 9])      # True  — 5 ada di dalam list
print(5 not in [1, 2, 3])  # True  — 5 tidak ada di dalam list

# Operator identitas
x = [1, 2]
y = x        # y menunjuk ke objek yang SAMA
z = [1, 2]   # z adalah objek BERBEDA meski nilainya sama

print(x is y)   # True  — objek sama
print(x is z)   # False — objek berbeda
print(x == z)   # True  — nilainya sama

# 3. RANGKUMAN

# - // untuk pembagian bulat, % untuk sisa bagi.
# - += dan -= mempersingkat penulisan penugasan.
# - in mengecek apakah nilai ada dalam list/string/dll.
# - is mengecek identitas objek, bukan kesamaan nilai.