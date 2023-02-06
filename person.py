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
        if re.fullmatch(re.compile(
                r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"),
                        value):
            return value
        else:
            raise ValueError('Is not correct mail!')


class Phone(Contact):

    @pydantic.validator('home', 'work')
    def is_correct(cls, value):
        if re.fullmatch(re.compile(r"\+?[1-9][0-9]{7,14}$"), value):
            return value
        else:
            raise ValueError('Is not correct phone!')


class Person(pydantic.BaseModel):
    id: int = random.getrandbits(32)
    name: Name
    mail: Mail
    phone: Phone
