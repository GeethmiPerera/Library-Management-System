class EduDVD:
    def __init__(self, DVD_no, title, subject, rental_price, copies):
        self.DVD_no = DVD_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


def statment(cd):
    print(f"Lecture dvd No: {cd.DVD_no}, Title: {cd.title}, Subject: {cd.subject}, Rental Price per day: {cd.rental_price}, Available number of copies:{cd.copies}")
    
    
class LibraryDVD:

    def __init__(self):
        self.dvd_list = []
        self.__initial_data()

    def __initial_data(self):
        dvd1 = EduDVD( 10, 'Birth of the Solar System', 'Astronomy', 2.50, 10)
        dvd2 = EduDVD(11, 'Pythagoras Theorem', 'Math', 1.00, 50)
        self.dvd_list.append(dvd1)
        self.dvd_list.append(dvd2)
    
    def add(self):
        dvd_no = input("Enter lecture dvd number:")
        if bool(dvd_no):
            Available_dvd = list(x for x in self.dvd_list if x.DVD_no == dvd_no)
            if len(Available_dvd) > 0:
                print("The DVD is available.")
                try:
                    copies = int(input("Number of copies:"))
                except ValueError:
                    print("Invalid Entry ")
                    return
                Available_dvd[0].copies += copies
                print("Added copies of DVD ")
            else:    
                title = input("Enter lecture dvd title:")
                subject = input("Enter lecture dvd Subject:")
                try:
                    rental_price = float(input("Enter lecture dvd rental price:"))
                    copies = int(input("Enter lecture dvd copies to add:"))
                except ValueError:
                    print(" Invalid Entry ")
                    return
    
                dvd = EduDVD(DVD_no = dvd_no, title = title, subject = subject, rental_price = rental_price, copies = copies)
                self.dvd_list.append(dvd)
                print("Lecture dvd added ")
            print()
    
    def remove(self):
        dvd_no = input("Enter lecture dvd number:")
        Available_dvd = list(x for x in self.dvd_list if x.DVD_no == dvd_no)
        if Available_dvd is None:
            print("Lecture dvd number not found.")
        for x in Available_dvd:
            self.dvd_list.remove(x)
            print("Lecture dvd Removed.")

    def lend(self):
        dvd_no = input("Enter lecture dvd number:")
        try:
            copies = int(input("Enter lent copies count:"))
        except ValueError:
            print("Invalid Entry ")
            return
        Available_dvd = list(x for x in self.dvd_list if x.DVD_no == dvd_no)
        for x in Available_dvd:
            x.copies -= copies
            print("Educatonal dvd Lent.")

    def receive(self):
        dvd_no = input("Enter dvd number:")
        try:
            copies = int(input("Enter received copies count:"))
        except ValueError:
            print("Invalid Entry ")
            return
            
        Available_dvd = list(x for x in self.dvd_list if x.DVD_no == dvd_no)
        for x in Available_dvd:
            x.copies += copies
            print("DVD received.")
            
    def available(self):
        Available_dvd = list(x for x in self.dvd_list if x.copies > 0)
        for x in Available_dvd:
            statment(cd=x)

    def unavailable(self):
        Available_dvd = list(x for x in self.dvd_list if x.copies == 0)
        for x in Available_dvd:
            statment(cd=x)

    def all(self, subject):
        for x in self.dvd_list:
            if x.subject == subject:
                statment(cd=x)



