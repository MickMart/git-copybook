from person import *
from book import *

import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)

while True:
    command = input('Enter command: ')

    if command == 'exit':
        with open('data.pickle', 'ab') as f:
            pickle.dump(data, f)
        break
    elif command == 'add':
        last_name = input('Enter last name: ')
        second_name = input('Enter second name: ')
        home_mail = input('Enter home mail : ')
        work_mail = input('Enter work mail: ')
        home_phone = input('Enter home phone: ')
        work_phone = input('Enter work phone: ')
        person = Person(name=Name(last_name=last_name, second_name=second_name),
                        mail=Mail(home=home_mail, work=work_mail),
                        phone=Phone(home=home_phone, work=work_phone))
        data.add(person)
        # for data in person:
        #     print(data)
        print(data.search)
    elif command == 'delete':
        value = input('ID or name: ').lower()
        if value == 'id':
            value = int(input('Enter ID: '))
            data.delete(contact_id=value)
        elif value == 'name':
            value = input('Enter name: ')
            data.delete(contact_name=value)
    elif command == 'search':
        value = input('ID or name: ').lower()
        if value == 'id':
            mm = int(input('Enter ID: '))
            data.search(contact_id=(mm, ))
        elif value == 'name':
            last_name = input('Enter last name: ')
            second_name = input('Enter second name: ')
            data.search(contact_name=(Name(last_name=last_name, second_name=second_name),))

