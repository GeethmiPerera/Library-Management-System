class Magazine:
    def __init__(self, magazine_no, title,Color, subject, rental_price, copies):
        self.magazine_no = magazine_no
        self.title = title
        self.color =Color
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


def statment(magazine):
    print(f"Magazine Number: {magazine.magazine_no}, Title: {magazine.title}, Color: {magazine.color}, Subject: {magazine.subject}, Rental Price per day: {magazine.rental_price}, Available Copies:{magazine.copies}")
    
    
class LibraryMagazine:
   
    def __init__(self):
        self.magazine_list = []
        self.__initial_data()

    def __initial_data(self):
        magazine1 = Magazine( 1, 'History of Cricket', 'color', 'Sports', 5.00, 7)
        magazine2 = Magazine(2, 'Evolution of the Computer', 'black&white', 'Technology', 3.00, 21 )

        magazine3 = Magazine(magazine_no="3", title="Title3",Color="Color print", subject="Sports", rental_price=32.50, copies=7)
        self.magazine_list.append(magazine1)
        self.magazine_list.append(magazine2)
        self.magazine_list.append(magazine3)

    def add(self):
        magazine_no = input("Enter Magazine Number:")
        if bool(magazine_no):
            Available_magazine = list(x for x in self.magazine_list if x.magazine_no == magazine_no)
            if len(Available_magazine) > 0:
                print("The magazine is available.")
                try:
                     copies= int(input("Number of copies:"))
                except ValueError:
                    print("Invalid Entry ")
                    return
                
                Available_magazine[0].copies += copies
                print("Added copies of magazine ")
        else:   
            title = input("Enter title:")
            color = input("Enter color :")
            subject = input(" Enter subject:")
            try:
                rental_price = float(input(" Enter rental price:"))
                copies = int(input(" Enter number of copies to add:"))
            except ValueError:
                print("Invalid Entry ")
                return

            magazine = Magazine(magazine_no = magazine_no, title = title,Color = color, subject = subject, rental_price = rental_price, copies = copies)
            self.magazine_list.append(magazine)
            print("Magazine added ")
            
        print()

    def remove(self):
        magazine_no = input("Enter magazine number:")
        Available_magazine = list(x for x in self.magazine_list if x.magazine_no == magazine_no)
        if Available_magazine is None:
            print("Magazine not found.")
        for x in Available_magazine:
            self.magazine_list.remove(x)
            print("Magazine Removed.")

    def lend(self):
        magazine_no = input("Enter magazine number:")
        try:
            copies = int(input("Enter lent copies count:"))
        except ValueError:
            print("Invalid Entry ")
            return
        Available_magazine = list(x for x in self.magazine_list if x.magazine_no == magazine_no)
        for x in Available_magazine:
            x.copies -= copies
            print(f" Magazine Lent.")

    def receive(self):
        magazine_no = input("Enter magazine number:")
        try:
            copies = int(input("Enter received copies count:"))
        except ValueError:
            print("Invalid Entry ")
            return
        Available_magazine = list(x for x in self.magazine_list if x.magazine_no == magazine_no)
        for x in Available_magazine:
            x.copies += copies
            print("Magazine received")
            
    def available(self):
        Available_magazine = list(x for x in self.magazine_list if x.copies > 0)
        for x in Available_magazine:
           statment(magazine=x)

    def unavailable(self):
        Available_magazine = list(x for x in self.magazine_list if x.copies == 0)
        for x in Available_magazine:
           statment(magazine=x)

    def all(self, subject):
        for x in self.magazine_list:
            if x.subject == subject:
               statment(magazine=x)



