class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks

    def display(self):
        if self.books==[]:
            print("Sorry! No more book available. Please try after some days!")
        else:
            print("Available books are:")    
            for book in self.books:
                print(" *" + book)
    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and returns it within 30 days!")
            self.books.remove(bookname)
            #return True
        
        else:
            print("Sorry! This book is either not available or has already been issued to someone else. Please wait until the book is available!")
            #return False
        
    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        req=input("Enter the name of the book you want to borrow: ")
        self.book=req
        return self.book.title()

    def returnBook(self):
        ret=input("Enter the name of the book you want to return or add: ")
        self.book=ret
        return self.book.title()

if __name__=="__main__":
    list=["Python", "Django", "Clrs", "Administrator"]
    centralLibrary=Library(list)
    #centralLibrary.display()
    student=Student()
    while True:
        welcomeMsg='''========Welcome to Central Library========
        1. Listing all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)

        a=int(input("Enter a choice:"))
        if a==1:
            centralLibrary.display()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
