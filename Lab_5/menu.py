"""
A menu - you need to add the database and fill in the functions. 
"""
from tkinter import Menu
from unicodedata import name
from Lab_5.menu_db import MenuDB

MenuDB.create_table()


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    all_records = MenuDB.get_all_records()
    print('All records: ')
    for row in all_records:
        print(row)


def add_new_record():
    name = input('What is the record holders name?: ')
    country = input('Where are they from?: ')
    catches = int(input('How many catches did they make?: '))
    MenuDB.make_new_record(name, country, catches)
    print('Record added')


def edit_existing_record():
    all_records = MenuDB.get_all_records()
    name = input('Whose record would you like to change?: ')
    for row in all_records:
        existing_name = row[0]
        if existing_name != name:
            print('no match found')
        else:
            catches = int(input('What is their new record?: '))
            MenuDB.edit_record(name, catches)


def delete_record():
    all_records = MenuDB.get_all_records()
    name = input('Whose record would you like to delete?: ')
    for row in all_records:
        existing_name = row[0]
        if existing_name != name:
            print('no match found')
        else:
            MenuDB.delete_record(name)


if __name__ == '__main__':
    main()