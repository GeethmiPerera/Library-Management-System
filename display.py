from book import LibraryBook
from magazine import LibraryMagazine
from dvd import LibraryDVD
from cd import LibraryCD

    
book_func =LibraryBook()
magazine_func =LibraryMagazine() 
dvd_func = LibraryDVD() 
cd_func = LibraryCD()


class Library:
    def __init__(self):
        self.magazine_list = []
        self.book_list = []
        self.dvd_list = []
        self.cd_list = []
        self._initial_data()

    def all(self, subject):
        resources = self.magazine_list + self.book_list + self.cd_list + self.dvd_list
        for y in resources:
            if subject in y.subject:
                print(y)

    def _initial_data(self):
        pass


 
def subject_list():
    print("subjects:")
    print('Science')
    print('History')
    print('Sports')
    print('Technology')
    print('Astronomy')
    print('Math')
    print('Music')
    print('Foreign Languages')
        
def display_massage():
    print("Welcome to the library system")
    print("1 - Add a new resource to the system ")
    print("2 - Remove e a resource from the system")
    print("3 - View currently available resources in each resource type")
    print("4 - View currently unavailable resources in each resource type ")
    print("5 - View all resources (any type) filtered by subject")
    print("6 - Lend a resource")
    print("7 - Update resource when received back. ")
    print("9 - Restart the program")
    print("0 - close the program")
    
       
def resource():
    selected_resource = 1
    while selected_resource > 0:
        try:
            selected_resource = int(input("Please select your option: "))
        except ValueError:
            print("Invalid Entry.")
            display_massage()

        if selected_resource == 1:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.add()
            elif resource_type == "magazine":
              magazine_func.add()
            elif resource_type == "cd":
              cd_func.add()
            elif resource_type == "dvd":
             dvd_func.add()

        elif selected_resource == 2:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.remove()
            elif resource_type == "magazine":
              magazine_func.remove()
            elif resource_type == "cd":
              cd_func.remove()
            elif resource_type == "dvd":
              dvd_func.remove()
            
        elif selected_resource == 3:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.available()
            elif resource_type == "magazine":
              magazine_func.available()
            elif resource_type == "cd":
              cd_func.available()
            elif resource_type == "dvd":
              dvd_func.available()
            
        elif selected_resource == 4:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.unavailable()
            elif resource_type == "magazine":
              magazine_func.unavailable()
            elif resource_type == "cd":
              cd_func.unavailable()
            elif resource_type == "dvd":
              dvd_func.unavailable()


        elif selected_resource == 5:
            subject_list()
            try:
                subject  = str(input('Enter subject choice: '))
                Library.all(subject)
            except ValueError:
                print('Invalid Entry: ')

        elif selected_resource == 6:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.lend()
            elif resource_type == "magazine":
              magazine_func.lend()
            elif resource_type == "dvd":
              cd_func.lend()
            elif resource_type == "cd":
              dvd_func.lend()

              
        elif selected_resource == 7:
            resource_type = input("Enter resouce type : (book, magazine,dvd or cd)")
            if resource_type == "book":
              book_func.receive()
            elif resource_type == "magazine":
              magazine_func.receive()
            elif resource_type == "cd":
              cd_func.receive()
            elif resource_type == "dvd":
              dvd_func.receive()
        elif selected_resource == 9:
            display_massage() 
        elif selected_resource== 0:
            print("Thank you .")
            quit()
        else:
            print("Invalid choice.")
            display_massage()

        if 1 <= selected_resource <= 7:
            input("Press Enter key to continue")
            display_massage()

display_massage()
resource()



