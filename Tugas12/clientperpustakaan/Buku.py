import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kodebuku = None
        self.__buku = None
        self.__penulis = None
        self.__penerbit = None
        self.__tahun = None
        self.__kategori = None
        self.__url = "http://localhost/perpustakaandata/buku_api.php"
                    
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
    def buku(self):
        return self.__buku
        
    @buku.setter
    def buku(self, value):
        self.__buku = value
    @property
    def penulis(self):
        return self.__penulis
        
    @penulis.setter
    def penulis(self, value):
        self.__penulis = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahun(self):
        return self.__tahun
        
    @tahun.setter
    def tahun(self, value):
        self.__tahun = value
    @property
    def kategori(self):
        return self.__kategori
        
    @kategori.setter
    def kategori(self, value):
        self.__kategori = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['idbk']
            self.__kodebuku = item['kodebuku']
            self.__buku = item['buku']
            self.__penulis = item['penulis']
            self.__penerbit = item['penerbit']
            self.__tahun = item['tahun']
            self.__kategori = item['kategori']
        return data
    def simpan(self):
        payload = {
            "kodebuku":self.__kodebuku,
            "buku":self.__buku,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kategori":self.__kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {
            "kodebuku":self.__kodebuku,
            "buku":self.__buku,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahun":self.__tahun,
            "kategori":self.__kategori
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodebuku(self,kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text