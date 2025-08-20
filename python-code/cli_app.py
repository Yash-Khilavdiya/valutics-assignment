print("Command Line - Library Book Manager")
class Book:
    # class variables
    books_title = []
    books_author = []
    books_publish_year = []
    books_isbn = []
    borrow_status = []
    books = dict()
    book_title = ""
    book_author = ""
    book_publish_year = ""
    book_isbn = ""
        
    def __init__(self):
        # print all books stored data
        #print(self.books_title)
        #print(self.books_author)
        #print(self.books_publish_year)
        #print(self.books_isbn)
        #print(self.borrow_status)
        pass
    
    def add_book(self):
        book_title  = input("Enter book Title : ")
        book_author  = input("Enter book author : ")
        book_publish_year  = input("Enter publish year : ")
        book_isbn  = input("Enter isbn number : ")
        print("Book title : ", book_title)
        print("Book author : ", book_author)
        print("Book publish year : ", book_publish_year)
        print("Books ISBN" , book_isbn)
        self.books_title.append(book_title)
        self.books_author.append(book_author)
        self.books_publish_year.append(book_publish_year)
        self.books_isbn.append(book_isbn)
        self.borrow_status.append(0)
        #print(self.books_title)
        #print(self.books_author)
        #print(self.books_author)
        #print(self.books_publish_year)
       # print(self.borrow_status)

    def list_all_books(self):
        # print all books stored data
        print("All Books : ", self.books_title)
        print("Books Authors : ", self.books_author)
        print("Publish Years: ", self.books_publish_year)
        print("Books ISBN", self.books_isbn)
        print("Books borrow status : ", self.borrow_status)
    
    def search_for_book(self):
        # search a book from all the books data based on title author or year published
        search_str = input("Search Book Name or other details : ")
        print("Searching for : ", search_str)
        
        # searching for string or integer from list using a list function
        searched_books_results = self.books_title.find(search_str)
        searched_authors_results = self.books_author.find(search_str)
        searched_publish_years_results = self.books_publish_year.find(search_str)
        print(searched_books_results)
        print(searched_authors_results)
        print(searched_publish_years_results)
    
    def borrow_or_return_a_book(self):
        book_to_borrow = int(input("Select book index which you want to borrow : "))
        if (self.borrow_status[book_to_borrow] == 1) : 
            print("Book is currently borrowed by someone.")
        else:
            self.borrow_status[book_to_borrow] == 1
            print("Book alloted to you successfully. Now you can read it.")
    
    def save_and_load_data(self):
        # for txt, json, csv or json data or file storing and fetching data from there ... 
        print()


class LibraryManager:

    def __init__(self):
        print()


# Add new books
book1 = Book()
lb = LibraryManager()

print("Menu : ")
opt_selected = int(input("Enter 1 for adding new book.\nEnter 2 for displaying all the books.\nEnter 4 for displaying all the books.\n"))

if opt_selected == 1:
    book1.add_book()
elif opt_selected == 2:
    book1.list_all_books()
elif opt_selected == 3:
    book1.borrow_or_return_a_book()
else:
    book1.search_for_book()

# list all books
# Serarch for books
# borrow or return a book
# save and load book   