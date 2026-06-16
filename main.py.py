from book import Book
from member import Member
from library import Library


def show_menu():
    print("\nLibrary Management System")
    print("1. Add book")
    print("2. Add member")
    print("3. View books")
    print("4. View members")
    print("5. Borrow book")
    print("6. Return book")
    print("7. View loans")
    print("8. Save and exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                genre = input("Genre: ")
                year = input("Year: ")

                book = Book(book_id, title, author, genre, year)
                library.add_book(book)
                print("Book added successfully.")

            elif choice == "2":
                member_id = input("Member ID: ")
                name = input("Name: ")
                email = input("Email: ")

                member = Member(member_id, name, email)
                library.add_member(member)
                print("Member added successfully.")

            elif choice == "3":
                for book in library.books:
                    print(book)

            elif choice == "4":
                for member in library.members:
                    print(member)

            elif choice == "5":
                book_id = input("Book ID: ")
                member_id = input("Member ID: ")

                library.borrow_book(book_id, member_id)
                print("Book borrowed successfully.")

            elif choice == "6":
                book_id = input("Book ID: ")

                library.return_book(book_id)
                print("Book returned successfully.")

            elif choice == "7":
                for loan in library.loans:
                    print(loan)

            elif choice == "8":
                library.save_all()
                print("Data saved. Goodbye.")
                break

            else:
                print("Invalid option. Please choose 1-8.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()