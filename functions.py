from book import Copybook
from person import *

import pickle


def greeting(option) -> [Copybook, str]:
    if option == 'create':
        book = Copybook()
    elif option == 'continue':
        file = input('Enter file name: ')
        book = load(file)
    else:
        return 'not correct'
    return book


def load(filename: str = 'book.bk') -> Copybook:
    with open(f'{filename}', 'rb') as filename:
        book = pickle.load(filename)

    return book


def save(obj: Copybook, filename: str = 'book.bk') -> str:
    with open(f'{filename}', 'ab') as file:
        pickle.dump(obj, file)

    return 'is correct!'


def add(obj: Copybook) -> Person:
    while True:
        try:
            first_name = input('Enter first name: ')
            second_name = input('Enter second name: ')
            middle_name = input('Enter middle name: ')
            name = Name(first_name=first_name, second_name=second_name, middle_name=middle_name)
            break
        except Exception as error:
            print(f"error: {error}")
    while True:
        try:
            home_mail = input('Enter home mail, if you have: ')
            work_mail = input('Enter work mail, if you have: ')
            mail = Mail(home=home_mail, work=work_mail)
            break
        except Exception as error:
            print(f"error: {error}")

    while True:
        try:
            home_phone = input('Enter home phone, if you have: ')
            work_phone = input('Enter work phone, if you have: ')
            phone = Phone(home=home_phone, work=work_phone)
            break
        except Exception as error:
            print(f"error: {error}")

    contact = Person(name=name,
                     mail=mail,
                     phone=phone)
    obj.add(contact)
    return contact


def delete(obj: Copybook, contact_id: int = None, contact_name: Name = None) -> str:
    obj.delete(contact_id, contact_name)
    return 'is correct'


def search(obj: Copybook, contact_id: int = None, contact_name: Name = None) -> str:
    obj.search(contact_id, contact_name)
    return 'is correct'


def list_book(obj: Copybook) -> str:
    obj.list_book()
    return 'is correct'
