from abc import abstractmethod
from Sayfa1 import mera
from Sayfa2 import inek,koyun,keci,tavuk
from Sayfa3 import dosya

class calisanlar():
    def __init__(self, ad, soyad, id, alan):
        self.ad = ad
        self.soyad = soyad
        self.id = int(id)
        self.alan = alan
        w.calisan_ekle(ad, soyad, id, alan)

    @abstractmethod
    def yem_ver(self):
        pass

    def su_ver(self):
        print("Su veriliyor..")


class calisan_inek(calisanlar):

    def inek_sag(self):
        inek.sut_litre += inek.adet * 15
        inek.stok["inek sütü"] = inek.sut_litre
        return int(inek.adet * 15)

    def yem_ver(self):
        return int(inek.adet * 10)

    def meraya_sal(self, mera_boyutu, adet):
        mera.meraya_Sal(self, mera_boyutu, adet)


class calisan_koyun(calisanlar):

    def koyun_sag(self):
        koyun.sut_litre += koyun.adet * 7
        koyun.stok["koyun sütü"] = koyun.sut_litre
        return int(koyun.adet * 7)

    def yem_ver(self):
        return int(koyun.adet * 5)

    def meraya_sal(self,mera_boyutu,adet):
        mera.meraya_Sal(self,mera_boyutu,adet)


class calisan_keci(calisanlar):

    def keci_sag(self):
        keci.sut_litre += keci.adet * 7
        keci.stok["keci sütü"] = keci.sut_litre
        return int(keci.adet * 7)


    def yem_ver(self):
        return int(keci.adet * 5)

    def meraya_sal(self, mera_boyutu, adet):
        mera.meraya_Sal(self, mera_boyutu, adet)


class calisan_tavuk(calisanlar):

    def yumurta_topla(self):
        tavuk.stok["yumurta"] += tavuk.adet
        return tavuk.adet

    def yem_ver(self):
        return int(tavuk.adet / 8)





w = dosya()

