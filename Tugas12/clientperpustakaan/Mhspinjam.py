import requests
import json
class Mhspinjam:
    def __init__(self):
        self.__id=None
        self.__kodebuku = None
        self.__ida = None
        self.__nama = None
        self.__jk = None
        self.__alamat = None
        self.__buku = None
        self.__peminjaman = None
        self.__pengembalian = None
        self.__url = "http://localhost/perpustakaandata/mhspinjam_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def ida(self):
        return self.__ida
        
    @ida.setter
    def ida(self, value):
        self.__ida = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def buku(self):
        return self.__buku
        
    @buku.setter
    def buku(self, value):
        self.__buku = value
    @property
    def peminjaman(self):
        return self.__peminjaman
        
    @peminjaman.setter
    def peminjaman(self, value):
        self.__peminjaman = value
    @property
    def pengembalian(self):
        return self.__pengembalian
        
    @pengembalian.setter
    def pengembalian(self, value):
        self.__pengembalian = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_ida(self, ida):
        url = self.__url+"?ida="+ida
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idprsp']
            self.__kodebuku = item['kodebuku']
            self.__ida = item['ida']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__alamat = item['alamat']
            self.__buku = item['buku']
            self.__peminjaman = item['peminjaman']
            self.__pengembalian = item['pengembalian']
        return data
    def simpan(self):
        payload = {
            "kodebuku":self.__kodebuku,
            "ida":self.__ida,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat,
            "buku":self.__buku,
            "peminjaman":self.__peminjaman,
            "pengembalian":self.__pengembalian
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_ida(self, ida):
        url = self.__url+"?ida="+ida
        payload = {
            "kodebuku":self.__kodebuku,
            "ida":self.__ida,
            "nama":self.__nama,
            "jk":self.__jk,
            "alamat":self.__alamat,
            "buku":self.__buku,
            "peminjaman":self.__peminjaman,
            "pengembalian":self.__pengembalian
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_ida(self,ida):
        url = self.__url+"?ida="+ida
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text