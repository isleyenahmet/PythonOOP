#We create title and author of class
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"{self.title} by {self.author} ")


class User:
    def __init__(self,name):
        self.name = name

    def display_info(self):
        print(f"User: {self.name}")


class Student(User):
    def display_info(self):
        print(f"Student Name: {self.name}" )

class Teacher(User):
    def display_info(self):
        print(f"Teacher Name: {self.name}")


class Library:
    def __init__(self): #yeni bir nesene oluşturduğunda oluşan ilk default yer burası (__init__ mantığı çok önemli)
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self): #bunu yazman aslında  son fonksiyonun itr olarak dönmesine zemin bunu yazmak ZORUNDASIN
        return  iter(self.books) #kitapların neler olduğunu döndürür bir nevi for loop
    
    def show_books(self):
        print("Available Books:")
        for book in self.books:
            book.display_info()

#kitap ve öğretmen nesneleri
book1 = Book("Fareler ve İnsanlar", "John Steinbeck")
book2 = Book("Hayvan Çiftliği", "Gerge Orwell")

student1 = Student("Ahmet")
teacher1 = Teacher("Sema")

#Bilgileri görmek
student1.display_info()
teacher1.display_info()

#kütüphane işlemleri
book1.display_info()
book2.display_info()

library = Library() #Library den gerçek bir nesne oluşturduk ve bunu da library ye atadıkk
library.add_book(book1)
library.add_book(book2)

library.show_books()