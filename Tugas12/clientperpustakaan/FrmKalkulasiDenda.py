'''
Nama    : Rifki Fadilah
Kelas   : R1
NIM     : 210511011
'''

from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from tkinter.messagebox import NO

class KalkulasiDenda:
    def __init__(self, parent, title):
        self.parent = parent       

        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=5)
        mainFrame.pack(fill=BOTH, expand=NO)
#=============================================================================================
        Label(mainFrame, text="Masukkan data dengan benar!").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Masukkan Berapa Hari Terlambat:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keterangan=").grid(row=10, column=0,
            sticky=W, padx=5, pady=5)

#=============================================================================================

        self.txtTelat = Entry(mainFrame) 
        self.txtTelat.grid(row=1, column=1, padx=5, pady=5)  
        self.txtKeterangan = Entry(mainFrame) 
        self.txtKeterangan.grid(row=10, column=1, padx=5, pady=5)  

#=============================================================================================

        self.btnHitung = Button(mainFrame, text='Cek Denda',  fg= "white", bg="blue",
            command=self.onHitung)
        self.btnHitung.grid(row=11, column=0, padx=5, pady=5)




#=============================================================================================

    def onHitung(self, event=None):
        telat = int(self.txtTelat.get())
        
        kalkulasi = (2000 * telat) + 1000
        if (kalkulasi>=3000):
            keterangan='Wajar'
        elif (kalkulasi>=5000):
            keterangan='Lain Kali Tau Waktu'
        elif (kalkulasi>=7000):
            keterangan='Jangan Diulangin Lagi'
        elif (kalkulasi>=11000):
            keterangan='Tau Waktu dan Jangan Diulangin'
        else :
            keterangan='SP 3'
        self.txtTelat.delete(0,END)
        self.txtTelat.insert(END,str(kalkulasi))
        self.txtKeterangan.delete(0,END)
        self.txtKeterangan.insert(END,str(keterangan))


#=============================================================================================
    def onKeluar(self, event=None):

        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = KalkulasiDenda(root, "Menghitung Biaya Keterlambatan Pengembalian")
    root.mainloop()
