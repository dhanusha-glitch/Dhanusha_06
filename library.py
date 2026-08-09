# ------------------ Person Class (Base Class) ------------------

class Person:
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    def get_name(self):
        return self._name

    def get_id(self):
        return self._person_id


# ------------------ Member Class (Inheritance) ------------------

class Member(Person):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.__borrowed_books = []

    def borrow_book(self, book_title):
        if len(self.__borrowed_books) >= 3:
            print("Borrow limit reached (Maximum 3 books).")
            return False

        self.__borrowed_books.append(book_title)
        return True

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        return False

    def show_borrowed_books(self):
        if not self.__borrowed_books:
            print("No books borrowed.")
        else:
            print("Borrowed Books:", ", ".join(self.__borrowed_books))


# ------------------ Book Class ------------------

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True

    def display(self):
        status = "Available" if self.__available else "Borrowed"
        print(f"ID:{self.__book_id} | {self.__title} | {self.__author} | {status}")


# ------------------ Library Class (Composition) ------------------

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    # ---------- Book Operations ----------

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                if book.is_available():
                    self.books.remove(book)
                    print("Book removed.")
                else:
                    print("Cannot remove. Book is borrowed.")
                return
        print("Book not found.")

    def search_book(self, keyword):
        found = False
        print("\nSearch Result:")
        for book in self.books:
            if keyword.lower() in book.get_title().lower() or keyword.lower() in book.get_author().lower():
                book.display()
                found = True
        if not found:
            print("No matching book found.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nBooks in Library")
            for book in self.books:
                book.display()

    # ---------- Member Operations ----------

    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.")

    def remove_member(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                self.members.remove(member)
                print("Member removed.")
                return
        print("Member not found.")

    def find_member(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                return member
        return None

    # ---------- Borrow Book ----------

    def borrow_book(self, member_id, title):
        member = self.find_member(member_id)

        if member is None:
            print("Member not found.")
            return

        for book in self.books:
            if book.get_title().lower() == title.lower():
                if not book.is_available():
                    print("Book already borrowed.")
                    return

                if member.borrow_book(book.get_title()):
                    book.borrow()
                    print("Book borrowed successfully.")
                return

        print("Book not found.")

    # ---------- Return Book ----------

    def return_book(self, member_id, title):
        member = self.find_member(member_id)

        if member is None:
            print("Member not found.")
            return

        for book in self.books:
            if book.get_title().lower() == title.lower():
                if member.return_book(title):
                    book.return_book()
                    print("Book returned successfully.")
                else:
                    print("This member didn't borrow this book.")
                return

        print("Book not found.")


# ------------------ Main Program ------------------

library = Library("Central Library")

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Display Books")
    print("4. Add Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Show Member Borrowed Books")
    print("8. Remove Book")
    print("9. Remove Member")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        keyword = input("Enter title/author: ")
        library.search_book(keyword)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        member_id = input("Member ID: ")
        name = input("Member Name: ")
        library.add_member(Member(member_id, name))

    elif choice == "5":
        member_id = input("Member ID: ")
        title = input("Book Title: ")
        library.borrow_book(member_id, title)

    elif choice == "6":
        member_id = input("Member ID: ")
        title = input("Book Title: ")
        library.return_book(member_id, title)

    elif choice == "7":
        member_id = input("Member ID: ")
        member = library.find_member(member_id)
        if member:
            member.show_borrowed_books()
        else:
            print("Member not found.")

    elif choice == "8":
        title = input("Book Title: ")
        library.remove_book(title)

    elif choice == "9":
        member_id = input("Member ID: ")
        library.remove_member(member_id)

    elif choice == "0":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Try again.")