from customer import add_customer, remove_customer, register_customer
from book import add_book
from rental import rent_books, return_book


def main():
    while True:
        print("1. Dodaj nowego klienta")
        print("2. Usuń klienta")
        print("3. Zarejestruj nowego klienta")
        print("4. Dodaj nową książkę")
        print("5. Wypożycz książkę")
        print("6. Zwrot książki")
        print("7. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            remove_customer()
        elif choice == "3":
            register_customer()
        elif choice == "4":
            add_book()
        elif choice == "5":
            customer_id = input("Podaj ID klienta: ")
            book_titles = input("Podaj tytuły książek oddzielone przecinkami: ").split(",")
            rent_books(customer_id, *book_titles)
        elif choice == "6":
            customer_id = input("Podaj ID klienta: ")
            book_title = input("Podaj tytuł zwracanej książki: ")
            return_book(customer_id, book_title)
        elif choice == "7":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
            main()




