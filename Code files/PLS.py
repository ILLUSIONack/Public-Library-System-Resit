import json
import os
import csv

class PublicLibrary():
    def __init__(self):
        self.catalog = Catalog()
        self.loanAdministration = LoanAdministration()
        self.catalog.initBooks()
        self.loanAdministration.initCustomers()

    def makeBackup(self):
        with open("./data/data.json", "r") as fromFile, open("./backup/" + namefile + ".json", "w") as to:
            to.write(fromFile.read())
            fromFile.close()
            to.close()
            print("Successfully backed up the library!")

    def restoreBackup(self,name):
        files = os.listdir("./backup/")
        for file in files:
            file = file.strip(".json")
            if file == name:
                os.remove("./data/data.json")
                with open("./backup/" + name + ".json", "r") as fromFile, open("./data/data.json", "w") as to:
                    to.write(fromFile.read())
                    fromFile.close()
                    to.close()
                    return "Successfully restored the backup file " + name
        return "Failed to restore the backup file " + name


class LoanAdministration():
    def __init__(self):
        self.loanItem = []
        self.customers = []
        self.loanItemPerBook = {}


    def addCustomer(self,gnd,ns,gn,surn,ad,zip,cty,email,user,tele):
        self.customers.append(Customer(gnd,ns,gn,surn,ad,zip,cty,email,user,tele))

    def checkAvailabilityBook(self,book):
        pass

    def borrowBook(self,customer,book):
        pass

    def returnBook(self,customer,book):
        pass

    def initCustomers(self):
        with open('./Code files/customers.csv','r') as csv_file:
            read = csv.reader(csv_file)
            for line in read:
                self.customers.append(Customer(line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10]))
            print("Customers Added")


class Person():
    def __init__(self,gnd,ns,gn,surn,ad,zip,cty,email,user,tele):
        self.gender = gnd
        self.nameSet = ns
        self.givenName = gn
        self.surName = surn
        self.adress = ad
        self.zipCode = zip
        self.city = cty
        self.email = email
        self.userName = user
        self.telefoon = tele


class Customer(Person):
    personid = 12345
    @staticmethod
    def gennumber():
            Customer.personid +=1
            return Customer.personid

    def __init__(self,gnd,ns,gn,surn,ad,zip,cty,email,user,tele):
        super().__init__(gnd,ns,gn,surn,ad,zip,cty,email,user,tele)
        self.id = Customer.gennumber()
        self.books = []

    def getCustomerName(self):
        return self.givenName
        
    
    def showBorrowedBooks(self):
        pass


class Author(Person):
    def __init__(self,gn,gnd='',ns='',surn='',ad='',zip='',cty='',email='',user='',tele=''):
        super().__init__(gnd,ns,gn,surn,ad,zip,cty,email,user,tele)

    def authorName(self):
        return self.givenName


class Book():
    bookid = 12345
    @staticmethod
    def gennumber():
            Book.bookid +=1
            return Book.bookid
        
    def __init__(self, author,country,imageLink,language,link,pages,title,year):
            self.bookid = Book.gennumber()
            self.author = []
            self.addAuthor(author)
            self.country = country
            self.imageLink = imageLink
            self.language = language
            self.link = link
            self.pages = pages
            self.title = title
            self.year = year

    def addAuthor(self,author):
        self.author.append(Author(author))
    
    def bookTitle(self):
        return self.title


class Catalog(Book):
    def __init__(self):
        self.books = []
        self.bookItems = []
        self.index = {}
        self.availableBookItems = {}

    def searchBook(self,input):
        for bookitem in self.bookItems:
            if input == bookitem.getTitle():
                print( "Book called '" +bookitem.getTitle() + "' found!")
            elif input == bookitem.getAuthor():
                print("Book: "+ bookitem.getTitle() +", Author: " +bookitem.getAuthor())


    def addBookItem(self,author,country,imageLink,language,link,pages,title,year):
        self.bookItems.append(BookItem(author,country,imageLink,language,link,pages,title,year))
    
    def initBooks(self):
        with open('./Code files/bookset.json','r') as json_file:
            read_books = json.load(json_file)
            for x in read_books:
                self.books.append(Book(x['author'],x['country'],x['imageLink'],x['language'],x['link'],x['pages'],x['title'],x['year']))
                self.bookItems.append(BookItem(x['author'],x['country'],x['imageLink'],x['language'],x['link'],x['pages'],x['title'],x['year']))
            print('Books and BookItems added.')
           

class BookItem(Book):
    def __init__(self,author,country,imageLink,language,link,pages,title,year):
        super().__init__(author,country,imageLink,language,link,pages,title,year)
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author[0].authorName()


class LoanItem(Book):
    pass
        

if __name__ == "__main__":
    PublicLibrary = PublicLibrary()
    #Search for a book called 'Things Fall Apart'
    PublicLibrary.catalog.searchBook("Things Fall Apart")
    #Search for a books with the author name 'Chinua Achebe'
    PublicLibrary.catalog.searchBook("Chinua Achebe")
    #Customer Name test
    print(PublicLibrary.loanAdministration.customers[0].getCustomerName())
    


