class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "miaaaawwwww")
class kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Cat!")
KucingA = kucing("Cat", 2, "Sherpa")
KucingA.bergerak() # output: cat bergerak
KucingA.bersuara() # output: Cat!
