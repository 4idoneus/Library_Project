class Library:
    def __init__(self):
        pass

    def __del__(self):
        # Close the file when the object is destroyed
        self.file.close()

    def list_books(self):
        print("--- Listing Books ---\n")
        try:
            # Open the file in "a+" mode
            self.file = open("books.txt", "a+")
            # Dosyanın içeriğini oku ve her satırı bir listeye ekle
            self.books = self.file.read().splitlines() 

            for book in self.books:
                title, author, *_ = book.split(",")
                print(f" {title}, {author}")
        
        except FileNotFoundError:
            print("There are no books in the library.") 

    def add_book(self):
        name = input("Book's Name: ")
        author = input("Author's Name: ")
        pages = input("How many pages does your book have?: ")
        publishing_year = input("Book's Publishing Year: ")
        genre = input("Book's Genre: ")

        # Write book information to the file
        self.file.write(f"{name},{author},{pages},{publishing_year},{genre}\n")
        print("\nBook added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        try:
            # Find the index of the book to be deleted
            index_to_remove = -1
            for i, book in enumerate(self.books):
                title, _, *_ = book.split(",")
                if title == title_to_remove:
                    index_to_remove = i
                    break
            
            if index_to_remove != -1:
                # Remove the book from the list
                self.books.pop(index_to_remove)
                # Remove the contents of the books.txt
                self.file.truncate(0)
                # Write the updated books to the file
                for book in self.books:
                    self.file.write(f"{book}\n")
                print("\nBook removed successfully.")
            else:
                print("Book not found.")
        except Exception as e:
            print(f"Error: {e}")

# main menu

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()

    elif choice == "2":
        lib.add_book()

    elif choice == "3":
        lib.remove_book()

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

