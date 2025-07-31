class Yarisma:
    def __init__(self,yarismaAdi):
        self.yarismaAdi = yarismaAdi

    def __str__(self):
        return self.yarismaAdi

class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

class student(person):
    def __init__(self,name,surname,stNumber):
        super().__init__(name,surname)
        self.stNumber = stNumber

    def display_info(self):
        print(f"{self.name} {self.surname} isimli öğrencinin numarasi: {self.stNumber} ")

class teacher(person):
    def __init__(self,name,surname,tcNumber):
        super().__init__(name,surname)
        self.tcNumber = tcNumber

    def display_info(self):
        print(f"{self.name} {self.surname} isimli ogretmenin numarasi: {self.tcNumber}" )

class School:
    def __init__(self):
        self.yarismaAdi = []

    def ekle_yarisma(self,yarisma):
        self.yarismaAdi.append(yarisma)

    def __iter__(self):
        return iter(self.yarismaAdi) #sonraki kod satırı için yaptığım hazırlık
    
    def goster_yarismalari(self):
        print("Yarisma Adlari: ")
        for yarisma in self.yarismaAdi:
            print(yarisma)


ogrenci1 = student("Ahmet", "İşleyen", "2020")
ogretmen1 = teacher("Sema", "Nur", "2021")
yarisma1 = Yarisma("Ucak Yarismasi")
yarisma2 = Yarisma("Araba Yarismasi")

okul = School() #önce bir nesne oluşturalım ve bunun üzerinden eklemeler yapalım
"""
okul.ekle_yarisma(yarisma1)
okul.ekle_yarisma(yarisma2) 
okul.goster_yarismalari()"""

student.display_info(ogrenci1)
teacher.display_info(ogretmen1)