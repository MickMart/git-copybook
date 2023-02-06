from book import Copybook
from person import *

import pickle


def greeting(option) -> str:
    if option == 'create':
        book = Copybook()
    elif option == 'continue':
        file = input('Enter file name: ')
        load(file)
    return 'is correct'


def load(filename: str = 'book.bk') -> Copybook:
    with open(f'{filename}', 'rb') as filename:
        book = pickle.load(filename)

    return book


def save(obj: Copybook, filename: str = 'book.bk') -> str:
    with open(f'{filename}', 'ab') as file:
        pickle.dump(obj, file)

    return 'is correct!'


def add(obj: Copybook, first_name: str, second_name: str, middle_name: str, home_mail: str = '', work_mail='',
        home_phone='', work_phone='') -> str:
    contact = Person(name=Name(first_name=first_name, second_name=second_name, middle_name=middle_name),
                     mail=Mail(home=home_mail, work=work_mail),
                     phone=Phone(home=home_phone, work=work_phone))
    obj.add(contact)
    return 'is correct'


def delete(obj: Copybook, contact_id: int = None, contact_name: Name = None) -> str:
    obj.delete(contact_id, contact_name)
    return 'is correct'


def search(obj: Copybook, contact_id: int = None, contact_name: Name = None) -> str:
    obj.search(contact_id, contact_name)
    return 'is correct'


def list_book(obj: Copybook) -> str:
    obj.list_book()
    return 'is correct'
