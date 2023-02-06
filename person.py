import re
import random
import pydantic


class Name(pydantic.BaseModel):
    first_name: str
    second_name: str
    middle_name: str


class Contact(pydantic.BaseModel):
    home: str = ''
    work: str = ''


class Mail(Contact):

    @pydantic.validator('home', 'work')
    def is_correct(cls, value):
        if value != '':
            if re.match(
                    f'^((([0-9A-Za-z]{1}[-0-9A-z\.]{0, 30}[0-9A-Za-z]?)|([0-9А-Яа-я]{1}[-0-9А-я\.]{0, 30}[0-9А-Яа-я]?))@([-A-Za-z]{1,}\.){1,}[-A-Za-z]{2,})$',
                    value):
                print('Is not correct mail!')
        return value


class Phone(Contact):

    @pydantic.validator('home', 'work')
    def is_correct(cls, value):
        if value != '':
            if re.match(f'/^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10, 14}(\s*)?$/', value):
                print('Is not correct phone!')
        return value


class Person(pydantic.BaseModel):
    id: int = random.getrandbits(32)
    name: Name
    mail: Mail
    phone: Phone
