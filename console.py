from book import Copybook
import functions as func


greeting = input('Enter create or continue: ')
book = func.greeting(greeting)

if book != 'not correct':
    while True:
        try:
            print('\ncommands {\nadd\ndelete\nsearch\nlist\n}\n')
            com = input('Enter command: ')
            if com == 'exit':
                func.save(book)
                break
            elif com == 'add':
                per = func.add(book)
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
