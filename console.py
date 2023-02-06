from book import Copybook
import functions as func


greeting = input('Enter create or continue: ')
book = func.greeting(greeting)

if book != 'not correct':
    while True:
        try:
            print('commands {\nadd\ndelete\nsearch\nlist\n}')
            com = input('Enter command: ')
            if com == 'exit':
                func.save(book)
                break
            elif com == 'add':
                first_name = input('Enter first name: ')
                second_name = input('Enter second name: ')
                middle_name = input('Enter middle name: ')
                home_mail = input('Enter home mail, if you have: ')
                work_mail = input('Enter work mail, if you have: ')
                home_phone = input('Enter home phone, if you have: ')
                work_phone = input('Enter work phone, if you have: ')
                per = func.add(book, first_name, second_name, middle_name, home_mail, work_mail, home_phone, work_phone)
                for data in per:
                    print(data)
            elif com == 'delete':
                option = input('ID or name: ').lower()
                if option == 'id':
                    value = int(input('Enter id: '))
                    print(func.delete(contact_id=value))
                elif option == 'name':
                    value = input('Enter id: ')
                    print(func.delete(contact_name=value))
                else:
                    print('Not correct')
            elif com == 'search':
                option = input('ID or name: ').lower()
                if option == 'id':
                    value = int(input('Enter id: '))
                    print(func.search(contact_id=value))
                elif option == 'name':
                    value = input('Enter id: ')
                    print(func.search(contact_name=value))
                else:
                    print('Not correct')
            elif com == 'list':
                func.list_book(book)
        except KeyboardInterrupt:
            func.save(book)
