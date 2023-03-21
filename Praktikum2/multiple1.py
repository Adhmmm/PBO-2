class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def presentasi(self):
        print(self.nama, "Sedang Mancing")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "Mancing pinggir sungai")
mhs_pekerja = MahasiswaPekerja("Adhim", "2105111050", "Mancing")
mhs_pekerja.presentasi() # output: Adhim sedang Mancing
mhs_pekerja.presentasi() # output: Adhim sedang Mancing
mhs_pekerja.bersosialisasi() # output: Adhim sedang bersosialisasi