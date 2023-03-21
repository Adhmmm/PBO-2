class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang memakan buah.")
class mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim= nim
    def menjelaskan(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang membersihkan tempat makan.")
mahasiswaA = mahasiswa("Adhim", 35, "210511050")
mahasiswaA.berbicara() # Output: adhim sedang memakan buah.
mahasiswaA.menjelaskan() # Output: adhim dengan NIM 210511150 sedang membersihkan tempat makan.