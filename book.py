class Book:
    def __init__(self, isbn_no, title, format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies 

def statment(book):
    print(f"ISBN NO: {book.isbn_no}, Title: {book.title}, Format: {book.format}, Subject: {book.subject}, Rental Price per day: {book.rental_price}, Available Copies:{book.copies}")
        
class LibraryBook:
    
    def __init__(self):
        self.book_list = []
        self.__initial_data()

    def __initial_data(self):
        b1 = Book('ISBN1234', 'The Solar System','Hardcover', 'Science', 15.00, 5)
        b2 = Book(' ISBN9876', 'Types of Animal Species','Paperback', 'Science', 10.00, 8)
        b3 = Book( 'ISBN1290', 'Second World War', 'Hardcover', 'History', 12.50, 1)
        self.book_list.append(b1)
        self.book_list.append(b2)
        self.book_list.append(b3)

    def add(self):
        isbn = input("Enter ISBN number:")
        if bool(isbn):
            Available_books = list(x for x in self.book_list if x.isbn_no == isbn)
            if len(Available_books) > 0:
                print("The book is available.")
                try:
                   copies = int(input("Number of copies:"))
                except ValueError:
                    print("Invalid Entry")
                    return
                
                Available_books[0].copies +=copies
                print("Added copies of the book ")
            
            else:           
                title = input(" Enter the title:")
                format = input(" Enter the format:")
                subject = input(" Enter the subject:")
                try:
                    rental_price = float(input(" Enter the rental price:"))
                    copies = int(input(" Enter number of copies to add:"))
                except ValueError:
                    print("Invalid Entry ")
                    return

                book = Book(isbn_no=isbn, title=title, format=format, subject=subject, rental_price=rental_price, copies=copies)
                self.book_list.append(book)
                print("Book added ")  
            print()

    def remove(self):
        isbn = input("Enter the  ISBN number:")
        Available_books = list(x for x in self.book_list if x.isbn_no == isbn)
        if Available_books is None:
            print("Book with ISBN number not found.")
        for x in Available_books:
            self.book_list.remove(x)
            print("Book Removed.")

    def lend(self):
        isbn = input("Enter ISBN number:")
        try:
           copies = int(input("Enter lend copies count:"))
        except ValueError:
            print("invalid Entry")
            return
        
        Available_books = list(x for x in self.book_list if x.isbn_no == isbn)
        for x in Available_books:
            x.copies -=copies
            print(" Book Lent")

    def receive(self):
        isbn = input("Enter ISBN number:")
        try:
           copies = int(input("Enter received copies count:"))
        except ValueError:
            print("Invalid Entry")
            return
        
        Available_books = list(x for x in self.book_list if x.isbn_no == isbn)
        for x in Available_books:
            x.copies +=copies
            print("Book received ")
            
    def available(self):
        Available_books = list(x for x in self.book_list if x.copies > 0)
        for x in Available_books:
            statment(book=x)

    def unavailable(self):
        Available_books = list(x for x in self.book_list if x.copies == 0)
        for x in Available_books:
            statment(book=x)

   
    def all(self, subject):
        if bool(subject):
            print(f"Filter By {subject}")
            for x in self.book_list:
                if x.subject == subject:
                    statment(book=x)
        


