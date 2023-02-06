from person import *


class Copybook:

    def __init__(self) -> None:
        self.data: list[Person] = []

    def add(self, contact: Person) -> None:
        if contact in self.data:
            print('There is already such a contact!')
        else:
            self.data.append(contact)

    def delete(self, contact_id: int = None, contact_name: Name = None) -> None:
        if contact_id is not None:
            for contact in self.data:
                if contact.id == contact_id:
                    self.data.remove(contact)
        elif contact_name is not None:
            for contact in self.data:
                if contact.name == contact_name:
                    self.data.remove(contact)
        else:
            print('Enter ID or name!')

    def search(self, contact_id: int = None, contact_name: Name = None) -> None:
        if contact_id is not None:
            for contact in self.data:
                if contact.id == contact_id:
                    for d in contact:
                        print(d)
        elif contact_name is not None:
            for contact in self.data:
                if contact.name == contact_name:
                    for d in contact:
                        print(d)
        else:
            print('Enter ID or name!')

    def list_book(self) -> None:
        for contact in self.data:
            for data in contact:
                print(data)
