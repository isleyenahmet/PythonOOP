class Urun:
    def __init__(self,urunAdi,adet,barkodNo):
        self.urunAdi = urunAdi
        self.adet = adet
        self.barkodNo = barkodNo
        
        def __str__(self):
            f"{self.urunAdi}, {self.adet}, {self.barkodNo}"

def urun_ekle(market):
    urunAdi = input("Urun Adi: ")
    adet = input("Adet: ")
    barkodNo = input("Barkod No: ")
    yeni_urun = Urun(urunAdi,adet,barkodNo)
    market.append(yeni_urun)
    print("Yeni Urun Basariyle Eklendi :)")

def urun_sil(market):
    if not market:
        print("Markette Ürün Bulunmuyor")
        return
    
    urun_listele(market)
    try:
        secim = input("Silinecek Ürün Numarasi: ")
        if 0 <=  secim < len(market):
            silinen = market.pop(secim)
            print(f"{silinen}, silindi.")
        else:
            print("Bu numarada bir ürün yok!")
    except ValueError:
        print("Gecersiz Deger!")

def urun_listele(market):
    if not market:
        print("Markette Listelenecek Ürün Yok")
        return
    else:
        for i,urn in enumerate(market):
            print(f"{i}: {urn}")
        print()



def anaMenu():
    market = []

    while(True):
        print("## Market Uygulamasina Hoş Geldiniz ##")
        print("1- Ürün Ekle")
        print("2- Ürün Sil")
        print("3- Tüm Ürünleri Listele")
        print("4- Çikis Yap")

        secim = input("Secim: ")

        if secim == "1":
            urun_ekle(market)
        elif secim == "2":
            urun_sil(market)
        elif secim == "3":
            urun_listele(market)
        elif secim == "4":
            print("Cikis Yapiliyor")
            break
        else:
            print("Gecerli Bir Deger Giriniz!")


anaMenu()