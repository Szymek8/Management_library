import csv
import os
from datetime import date


def rent_books(customer_id, *book_titles):
    rental_date = date.today().strftime("%Y-%m-%d")

    with open('book.csv', mode='r') as book_file:
        books = list(csv.reader(book_file))

    rented_books = []
    for title in book_titles:
        book_found = False
        for i in range(len(books)):
            if books[i][0].upper() == title.upper():
                rented_books.append(title)
                books.pop(i)
                book_found = True
                break

        if not book_found:
            print(f"Książka '{title}' nie istnieje w bazie danych.")

    with open('book.csv', mode='w', newline='') as book_file:
        writer = csv.writer(book_file)
        writer.writerows(books)

    if rented_books:
        file_path = f"DATABASE/{customer_id}.txt"
        with open(file_path, mode='a') as db_file:
            for book in rented_books:
                db_file.write(f"{rental_date}\t{book}\n")

        print("Książki wypożyczone.")
    else:
        print("Brak książek do wypożyczenia.")


def return_book(customer_id, book_title):
    file_path = f"DATABASE/{customer_id}.txt"
    temp_file_path = f"DATABASE/{customer_id}_temp.txt"

    found = False

    with open(file_path, mode='r') as db_file, open(temp_file_path, mode='w') as temp_file:
        for line in db_file:
            if book_title.upper() in line.upper():
                found = True
            else:
                temp_file.write(line)

    if found:
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
        print("Książka zwrócona.")
    else:
        os.remove(temp_file_path)
        print("Nie znaleziono wypożyczonej książki.")


