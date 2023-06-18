import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mhspinjam import *
class FrmMhspinjam:
    
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
        Label(mainFrame, text='Isi Data Dengan Sebenar - benarnya').grid(row=9, column=3,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='IDA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BUKU:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PEMINJAMAN:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENGEMBALIAN:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=0, column=1, padx=5, pady=5)
        # Textbox
        self.txtIda = Entry(mainFrame) 
        self.txtIda.grid(row=1, column=1, padx=5, pady=5)
        self.txtIda.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtJk = Entry(mainFrame) 
        self.txtJk.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtBuku = Entry(mainFrame) 
        self.txtBuku.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtPeminjaman = Entry(mainFrame) 
        self.txtPeminjaman.grid(row=6, column=1, padx=5, pady=5)
        # Textbox
        self.txtPengembalian = Entry(mainFrame) 
        self.txtPengembalian.grid(row=7, column=1, padx=5, pady=5)
        # Button
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, fg= "white", bg="green")
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg= "white", bg="blue")
        self.btnSimpan.grid(row=8, column=0, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, fg= "black", bg="yellow")
        self.btnClear.grid(row=8, column=1, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg= "white", bg="red")
        self.btnHapus.grid(row=8, column=2, padx=5, pady=5)
        # define columns
        columns = ('idprsp','kodebuku','ida','nama','jk','alamat','buku','peminjaman','pengembalian')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idprsp', text='No')
        self.tree.column('idprsp', width="20")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="70")
        self.tree.heading('ida', text='IDA')
        self.tree.column('ida', width="70")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="60")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="80")
        self.tree.heading('buku', text='BUKU')
        self.tree.column('buku', width="150")
        self.tree.heading('peminjaman', text='PEMINJAMAN')
        self.tree.column('peminjaman', width="120")
        self.tree.heading('pengembalian', text='PENGEMBALIAN')
        self.tree.column('pengembalian', width="120")
        # set tree position
        self.tree.place(x=0, y=320)
        
    def onClear(self, event=None):
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtIda.delete(0,END)
        self.txtIda.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk.delete(0,END)
        self.txtJk.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,"")
        self.txtPeminjaman.delete(0,END)
        self.txtPeminjaman.insert(END,"")
        self.txtPengembalian.delete(0,END)
        self.txtPengembalian.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mhspinjam
        obj = Mhspinjam()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idprsp"],d["kodebuku"],d["ida"],d["nama"],d["jk"],d["alamat"],d["buku"],d["peminjaman"],d["pengembalian"]))
    def onCari(self, event=None):
        ida = self.txtIda.get()
        obj = Mhspinjam()
        a = obj.get_by_ida(ida)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        ida = self.txtIda.get()
        obj = Mhspinjam()
        res = obj.get_by_ida(ida)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtIda.delete(0,END)
        self.txtIda.insert(END,obj.ida)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk.delete(0,END)
        self.txtJk.insert(END,obj.jk)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.txtBuku.delete(0,END)
        self.txtBuku.insert(END,obj.buku)
        self.txtPeminjaman.delete(0,END)
        self.txtPeminjaman.insert(END,obj.peminjaman)
        self.txtPengembalian.delete(0,END)
        self.txtPengembalian.insert(END,obj.pengembalian)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodebuku = self.txtKodebuku.get()
        ida = self.txtIda.get()
        nama = self.txtNama.get()
        jk = self.txtJk.get()
        alamat = self.txtAlamat.get()
        buku = self.txtBuku.get()
        peminjaman = self.txtPeminjaman.get()
        pengembalian = self.txtPengembalian.get()
        # create new Object
        obj = Mhspinjam()
        obj.kodebuku = kodebuku
        obj.ida = ida
        obj.nama = nama
        obj.jk = jk
        obj.alamat = alamat
        obj.buku = buku
        obj.peminjaman = peminjaman
        obj.pengembalian = pengembalian
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_ida(ida)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        ida = self.txtIda.get()
        obj = Mhspinjam()
        obj.ida = ida
        if(self.ditemukan==True):
            res = obj.delete_by_ida(ida)
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
    aplikasi = FrmMhspinjam(root2, "Pinjam Buku By Rifki F")
    root2.mainloop()