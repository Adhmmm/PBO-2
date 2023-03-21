class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang melaju.")
class Mobil(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Mobil ini sedang belok.")
mobilA = Mobil("Mobil", "Hyundai", "putih", 150)
mobilA.berkendara() # Output: Kendaraan ini sedang berjalan.
mobilA.belok() # Output: Sepeda motor ini sedang belok.
