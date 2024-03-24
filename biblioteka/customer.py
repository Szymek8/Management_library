import csv
import random
import os


def add_customer():
    name = input("Podaj imię i nazwisko klienta: ")
    address = input("Podaj adres klienta: ")

    customer_id = str(random.randint(100, 999))

    with open('customer.csv', mode='a', newline='') as customer_file:
        writer = csv.writer(customer_file)
        writer.writerow([customer_id, name])

    with open('address.csv', mode='a', newline='') as address_file:
        writer = csv.writer(address_file)
        writer.writerow([customer_id, address])

    print("Nowy klient dodany do bazy danych.")


def remove_customer():
    search_option = input("Wybierz opcję wyszukiwania (ID lub NAME): ")
    search_query = input("Podaj wartość wyszukiwania: ")

    if search_option.upper() == "ID":
        field_index = 0
    elif search_option.upper() == "NAME":
        field_index = 1
    else:
        print("Nieprawidłowa opcja wyszukiwania.")
        return

    customer_found = False

    with open('customer.csv', mode='r') as customer_file:
        customers = list(csv.reader(customer_file))

        with open('address.csv', mode='r') as address_file:
            addresses = list(csv.reader(address_file))

            for i in range(len(customers)):
                if customers[i][field_index].upper() == search_query.upper():
                    customer_id = customers[i][0]

                    customers.pop(i)
                    addresses.pop(i)

                    with open('customer.csv', mode='w', newline='') as customer_file:
                        writer = csv.writer(customer_file)
                        writer.writerows(customers)

                    with open('address.csv', mode='w', newline='') as address_file:
                        writer = csv.writer(address_file)
                        writer.writerows(addresses)

                    if os.path.exists(f"DATABASE/{customer_id}.txt"):
                        os.remove(f"DATABASE/{customer_id}.txt")

                    print("Klient usunięty z bazy danych.")
                    customer_found = True
                    break

    if not customer_found:
        print("Nie znaleziono klienta o podanych danych.")


def register_customer():
    name = input("Podaj imię i nazwisko klienta: ")

    customer_id = str(random.randint(100, 999))

    with open('customer.csv', mode='a', newline='') as customer_file:
        writer = csv.writer(customer_file)
        writer.writerow([customer_id, name])

    print("Nowy klient zarejestrowany.")

    # Create a database file for the customer
    file_path = f"DATABASE/{customer_id}.txt"
    with open(file_path, mode='w') as db_file:
        db_file.write("Data wypożyczenia\tTytuł książki\n")

    print(f"Utworzono plik bazy danych dla klienta o ID {customer_id}.")

