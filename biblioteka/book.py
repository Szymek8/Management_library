import csv


def add_book():
    title = input("Podaj tytuł książki: ")
    author = input("Podaj autora książki: ")

    with open('book.csv', mode='a', newline='') as book_file:
        writer = csv.writer(book_file)
        writer.writerow([title, author])

    print("Nowa książka dodana do bazy danych.")