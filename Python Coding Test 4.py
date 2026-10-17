class LBS:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        self.is_borrowed = True
        print(f"\n{self.title} (written by {self.author}) has not been borrowed.\nYou are allowed to borrow it.")

    def _return(self):
        self.is_borrowed = False
        print(f"\n{self.title} (written by {self.author}) has been borrowed.\nIt will have to be returned.")

first_name = input("\nEnter the first book you want to check for in the library:")
first_author = input("Enter the author of the book you have mentioned:")

first = LBS(first_name, first_author)

second_name = input("\nEnter the second book you want to check for in the library:")
second_author = input("Enter the author of the book you have mentioned:")

second = LBS(second_name, second_author)

third_name = input("\nEnter the third book you want to check for in the library:")
third_author = input("Enter the author of the book you have mentioned:")

third = LBS(third_name, third_author)

first.borrow()
second.borrow()
third.borrow()

print("\nRechecking Library Status...")

first._return()
second._return()
third._return()