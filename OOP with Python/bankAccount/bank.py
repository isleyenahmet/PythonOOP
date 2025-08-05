class BankAccount:
    def __init__(self,name,surname,id):
        self.name= name
        self.surname = surname
        self.id = id
        self.balance = 0 #başlangıç bakiyesi 0

    def __str__(self):
        return f"{self.name} {self.surname} adlı kullanicinin id'si {self.id} ve bakiyesi: {self.balace}"

def paraYatir(banka):
    idNo = input("ID Numaranizi Giriniz: ")
    for hesap in banka:
        if hesap.id == idNo:
            try:
                miktar =float(input("Eklemek İstediginiz Tutari Giriniz: "))
                if miktar <= 0:
                    print("Lutfen pozitif Bir miktar giriniz")
                    return
                hesap.balance += miktar
                print(f"{miktar} hesabiniza Yatirilmiştir!")
            except ValueError:
                print("Lufen Gecerli Bir Deger Giriniz!")
            return 
    print("Bu id ye sahip hesap bulunamadi")

    
def anaMenu():
    banka = []
    #Örnek Bazı Hesaplar
    banka.append(BankAccount("Ahmet","İşleyen",123))
    banka.append(BankAccount("SemaNur", "Caglar",124))

    secim = input("Secimi Giriniz: ")
    
    print("-*- Banka Uygulamasina Hoş Geldiniz -*-")
    print("1- Para Yatir")
    print("2- Para Çek")
    print("3- Tüm Bakiye Görüntüle")
    print("4- Çikiş Yap")

    while(True):
        if secim == "1":
            paraYatir(banka)
        elif secim == "2":
            paraCek(banka)
        elif secim == "3":
            bakiyeGoruntule(banka)
        elif secim == "4":
            print("Ugulamadan Cikis Yapiliyor!")
            break
        else:
            print("Lutfen Gecerli Bir deger Giriniz!")
