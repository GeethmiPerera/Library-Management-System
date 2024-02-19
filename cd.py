class LectCD:
    def __init__(self, CD_no, title, subject, rental_price, copies):
        self.CD_no = CD_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies


def statment(cd):
    print(f"Lecture Cd No: {cd.CD_no}, Title: {cd.title}, Subject: {cd.subject}, Rental Price per day: {cd.rental_price}, Available Copies:{cd.copies}")
    
    
class LibraryCD:


    def __init__(self):
        self.cd_list = []
        self.__initial_data()

    def __initial_data(self):
        cd1 = LectCD( 21,'Basics of Western Music', 'Music', 1.50, 11)
        cd2 = LectCD( 22, 'Japanese Language', 'Foreign Languages', 2.00, 3)
        self.cd_list.append(cd1)
        self.cd_list.append(cd2)
        
    def add(self):
        CD_num = input("Enter lecture cd number:")
        if bool(CD_num):
            matched_data = list(x for x in self.cd_list if x.CD_no ==CD_num)
            if len(matched_data) > 0:
                print("The lecture cd is available.")
                try:
                    copies = int(input("Number of copies:"))
                except ValueError:
                    print(" Invalid Entry")
                    return
                
                matched_data[0].copies += copies
                print("CD copies are added ")
        else:       
            title = input("Enter lecture cd title:")
            subject = input("Enter lecture cd Subject:")
            try:
                rental_price = float(input("Enter lecture cd rental price:"))
                copies = int(input("Enter lecture cd copies to add:"))
            except ValueError:
                print("Invalid Entry ")
                return

            cd = LectCD(CD_no =CD_num, title = title, subject = subject, rental_price = rental_price, copies = copies)
            self.cd_list.append(cd)
            print("Lecture Cd added")
        print()

    def remove(self):
        CD_num = input("Enter lecture cd number:")
        matched_data = list(x for x in self.cd_list if x.CD_no ==CD_num)
        if matched_data is None:
            print("Lecture Cd  not found.")
        for x in matched_data:
            self.cd_list.remove(x)
            print("Lecture Cd Removed.")

    def lend(self):
        CD_num = input("Enter lecture cd number:")
        try:
            copies = int(input("Enter lent copies count:"))
        except ValueError:
            print("Invalid Entry")
            return
        matched_data = list(x for x in self.cd_list if x.CD_no ==CD_num)
        for x in matched_data:
            x.copies -= copies
            print(" lecture cd Lent.")

    def receive(self):
        CD_num = input("Enter cd number:")
        try:
            copies = int(input("Enter received number of copies:"))
        except ValueError:
            print("Invalid Entry")
            return
        matched_data = list(x for x in self.cd_list if x.CD_no ==CD_num)
        for x in matched_data:
            x.copies += copies
            print("CD received.")
            
    def available(self):
        matched_data = list(x for x in self.cd_list if x.copies > 0)
        for x in matched_data:
            statment(cd=x)

    def unavailable(self):
        matched_data = list(x for x in self.cd_list if x.copies == 0)
        for x in matched_data:
            statment(cd=x)

    
    def display_all(self, subject):
        for x in self.cd_list:
            if x.subject == subject:
                statment(cd=x)



