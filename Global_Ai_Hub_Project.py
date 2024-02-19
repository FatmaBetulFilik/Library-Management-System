class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books_list = self.file.read().splitlines()

        for line in books_list:
            current_line = line.split(",")
            print(current_line[0:2])
        print("Books are listed successfully.")

    def add_book(self, title_book, author, release_year, page_number):

        if release_year.isnumeric() and page_number.isnumeric():
            if release_year > 0 and title_book.isalpha() and page_number > 0 and author.isalpha():
                book_str = "{},{},{},{}".format(title_book, author, release_year, page_number)
                self.file.write(book_str + "\n")
                print("Book is added successfully.")
            else:
                print("Please enter a valid value.")
        else:
            print("Please enter a valid value.")

    def remove_book(self, title):
        self.file.seek(0)
        books_list = self.file.read().splitlines()

        flag = 0
        for line in books_list:
            if line.split(",")[0] == title:
                index = books_list.index(line)
                del books_list[index]
                flag += 1

        self.file.seek(0)
        self.file.truncate()
        for item in books_list:
            self.file.write(item + "\n")
        if flag != 0:
            print("Book is removed successfully.")
        elif flag == 0:
            print("Book is not in the library.")


lib = Library()

while True:
    user_choice = int(input("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n"))
    if user_choice == 1:
        lib.list_books()
        break
    elif user_choice == 2:

        book_title = input("Please enter the book title: ")
        book_author = input("Please enter the authors name: ")
        book_release_year = input("Please enter release year: ")
        book_page_number = input("Please enter page number: ")

        lib.add_book(book_title, book_author, book_release_year, book_page_number)
        break
    elif user_choice == 3:

        book_name = input("Please enter a book title to be removed: ")
        lib.remove_book(book_name)
        break
    else:
        print("Your selection is not valid, please make another selection: ")
