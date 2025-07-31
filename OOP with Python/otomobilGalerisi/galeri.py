class Otomobil:
    def __init__(self,marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def __str__(self):
        return f"{self.marka}, {self.model}, {self.yil}"
    

def otomobilEkle(galeri):
    marka = input("Marka: ")
    model = input("Model: ")
    yil = input("Yil: ")
    yeniOtomobil = Otomobil(marka,model,yil)
    galeri.append(yeniOtomobil)
    print("Otomobil başariyla eklendi.\n")

def otomobilSil(galeri):
    if not galeri:
        print("Galeride Kayitli Arac Yok!")
        return

    otomobilListele(galeri)
    try:
        secim = int(input("Silmek İstediğiniz Otomobilin Numarasini Giriniz: "))
        if 0 <= secim < len(galeri):
            silinen = galeri.pop(secim)
            print(f"{silinen} silindi. \n")
        else:
            print("Gecersiz Secim!")
    except ValueError:
        print("Lutfen Gecerli Bir Deger Giriniz!")

def otomobilListele(galeri):
    if not galeri:
        print("Galeride Kayitli Arac Yok!")
        return
    else:
        print("Galerideki Otomobiller: \n")
        for i, oto in enumerate(galeri):
            print(f"{i}: {oto}")
        print()


def anaMenu():
    galeri = [] #Galeride tutulan araçlar için bu listede saklayacağimiz veriler

    while(True):
        
        print("## Galeri Uygulamamiza Hoş Geldiniz ##")
        print("1- Otomobil Ekle")
        print("2- Otomobil Sil")
        print("3- Otomobilleri Listele")
        print("4- Çikis Yap")

        secim = input("Seciminiz: ")

        if secim == "1":
            otomobilEkle(galeri)
        elif secim == "2":
            otomobilSil(galeri)
        elif secim == "3":
            otomobilListele(galeri)
        elif secim == "4":
            print("Hoscakalin...")
            break
        else:
            print("Gecersiz Secenek! Lutfen Tekrar Deneyiniz") 


anaMenu()