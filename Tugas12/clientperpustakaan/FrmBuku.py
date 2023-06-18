import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Daftar Buku di Perpustakaan').grid(row=7, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BUKU:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KATEGORI:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodebuku.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtBuku = Entry(mainFrame) 
        self.txtBuku.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtTahun = Entry(mainFrame) 
        self.txtTahun.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtKategori = Entry(mainFrame) 
        self.txtKategori.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, fg= "white", bg="green")
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg= "white", bg="blue")
        self.btnSimpan.grid(row=6, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, fg= "black", bg="yellow")
        self.btnClear.grid(row=6, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg= "white", bg="red")
        self.btnHapus.grid(row=6, column=2, padx=5, pady=5)
        # define columns
        columns = ('idbk','kodebuku','buku','penulis','penerbit','tahun','kategori')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idbk', text='IDBK')
        self.tree.column('idbk', width="20")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="70")
        self.tree.heading('buku', text='BUKU')
        self.tree.column('buku', width="150")
        self.tree.heading('penulis', text='PENULIS')
        self.tree.column('penulis', width="80")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="80")
        self.tree.heading('tahun', text='TAHUN')
        self.tree.column('tahun', width="50")
        self.tree.heading('kategori', text='KATEGORI')
        self.tree.column('kategori', width="80")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,"")
        self.txtKategori.delete(0,END)
        self.txtKategori.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idbk"],d["kodebuku"],d["buku"],d["penulis"],d["penerbit"],d["tahun"],d["kategori"]))
    def onCari(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        a = obj.get_by_kodebuku(kodebuku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        res = obj.get_by_kodebuku(kodebuku)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,obj.buku)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.penulis)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahun.delete(0,END)
        self.txtTahun.insert(END,obj.tahun)
        self.txtKategori.delete(0,END)
        self.txtKategori.insert(END,obj.kategori)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodebuku = self.txtKodebuku.get()
        buku = self.txtBuku.get()
        penulis = self.txtPenulis.get()
        penerbit = self.txtPenerbit.get()
        tahun = self.txtTahun.get()
        kategori = self.txtKategori.get()
        # create new Object
        obj = Buku()
        obj.kodebuku = kodebuku
        obj.buku = buku
        obj.penulis = penulis
        obj.penerbit = penerbit
        obj.tahun = tahun
        obj.kategori = kategori
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodebuku(kodebuku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        obj.kodebuku = kodebuku
        if(self.ditemukan==True):
            res = obj.delete_by_kodebuku(kodebuku)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmBuku(root2, "Data Buku By Rifki F")
    root2.mainloop()