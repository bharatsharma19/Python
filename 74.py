# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# BharatLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    bharat = Library(['1 - Python', '2 - Rich Dad Poor Dad', '3 - Harry Potter',
                      '4 - C++ Basics', '5 - Algorithms by CLRS', '6 - Amazing Secrets of life', '7 - The theory of Everything', '8 - The power of your Subconscious Mind', '9 - 12th fail'], "Bharat's")

    while(True):
        print(
            f"Welcome to the {bharat.name} library. Enter your choice to continue")
        print("1 -> Display Books")
        print("2 -> Lend a Book")
        print("3 -> Add a Book")
        print("4 -> Return a Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            bharat.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            bharat.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            bharat.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            bharat.returnBook(book)

        else:
            print("Not a valid option")

        print("Press Q to Quit and C to Continue")
        user_choice2 = ""
        while(user_choice2 != "C" and user_choice2 != "Q"):
            user_choice2 = input()
            if user_choice2 == "Q":
                exit()

            elif user_choice2 == "C":
                continue
