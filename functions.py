from book import Copybook
from person import Name



def search(data: Copybook):
    value = input('ID or name: ').lower()
    if value == 'id':
        mm = int(input('Enter ID: '))
        data.search(contact_id=(mm,))
    elif value == 'name':
        last_name = input('Enter last name: ')
        second_name = input('Enter second name: ')
        data.search(contact_name=(Name(last_name=last_name, second_name=second_name),))