# 1. KONSEP

# Inner class adalah class yang didefinisikan di dalam class lain.
# Digunakan saat dua class sangat erat hubungannya dan inner class
# tidak perlu dipakai di luar class induknya.
#
# Kapan pakai inner class:
# - Struktur pembantu yang hanya relevan untuk class induknya
# - Contoh umum: Node di dalam LinkedList, Address di dalam Customer

# 2. CONTOH

# Inner class dasar
class Perpustakaan:
    class Buku:                         # inner class
        def __init__(self, judul):
            self.judul = judul

        def info(self):
            return f"Buku: {self.judul}"

    def __init__(self):
        self.koleksi = []

    def tambah_buku(self, judul):
        buku_baru = Perpustakaan.Buku(judul)   # buat objek inner class
        self.koleksi.append(buku_baru)

    def tampilkan(self):
        for buku in self.koleksi:
            print(buku.info())

lib = Perpustakaan()
lib.tambah_buku("Bumi Manusia")
lib.tambah_buku("Laskar Pelangi")
lib.tampilkan()

# Membuat inner class langsung dari luar (jika perlu)
buku_luar = Perpustakaan.Buku("Perahu Kertas")
print(buku_luar.info())

# Contoh nyata: LinkedList dengan inner class Node
class LinkedList:
    class Node:                        # inner class — hanya untuk LinkedList
        def __init__(self, nilai):
            self.nilai   = nilai
            self.berikut = None        # menunjuk ke Node selanjutnya

    def __init__(self):
        self.kepala = None             # awal dari linked list

    def tambah(self, nilai):
        node_baru = LinkedList.Node(nilai)

        if self.kepala is None:        # list masih kosong
            self.kepala = node_baru
            return

        # Pergi ke node paling akhir, lalu sambungkan
        saat_ini = self.kepala
        while saat_ini.berikut is not None:
            saat_ini = saat_ini.berikut
        saat_ini.berikut = node_baru

    def tampilkan(self):
        hasil  = []
        saat_ini = self.kepala
        while saat_ini is not None:
            hasil.append(str(saat_ini.nilai))
            saat_ini = saat_ini.berikut
        print(" → ".join(hasil))

ll = LinkedList()
ll.tambah(10)
ll.tambah(20)
ll.tambah(30)
ll.tampilkan()   # 10 → 20 → 30

# 3. RANGKUMAN

# - Inner class adalah class yang didefinisikan di dalam class lain.
# - Gunakan saat class pembantu hanya relevan untuk class induknya.
# - Akses inner class lewat: NamaInduk.NamaInner()
# - Contoh nyata yang umum: Node di dalam LinkedList, Item di dalam Cart.