import csv
import os

FILENAME = "records.csv"

def create_file():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Marks"])
    print("CSV file created.")

def add_record():
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)

        id = input("Enter ID: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        writer.writerow([id, name, marks])
    print("Record added.")

def view_records():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        print("\nID   Name    Marks")
        for row in reader:
            print(row)

def search_record():
    search_id = input("Enter ID to search: ")

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ID"] == search_id:
                print("Record Found:", row)
                return

        print("Record not found.")

def update_record():
    rows = []

    update_id = input("Enter ID to update: ")

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == update_id:
                row[2] = input("Enter new marks: ")
            rows.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Record updated.")

# Main Program
if not os.path.exists(FILENAME):
    create_file()

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        update_record()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
