import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmCekbuku:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        
        # define columns
        columns = ('idbk','kodebuku','buku','penulis','penerbit','tahun','kategori')
        self.tree = ttk.Treeview(columns=columns, show='headings')
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
        self.tree.place(x=0, y=0)
        
    def onClear(self, event=None):
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

                 
        # create new Object
        obj = Buku()
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
    aplikasi = FrmCekbuku(root2, "Daftar Buku By Rifki F")
    root2.mainloop()