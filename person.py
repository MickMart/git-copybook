import re
import random
import pydantic


class Name(pydantic.BaseModel):
    last_name: str
    second_name: str
    otechstvo: str


class Contact(pydantic.BaseModel):
    home: str
    work: str


class Mail(Contact):

    @pydantic.validator('home', 'work')
    def is_correct(cls, value):
        return value


class Phone(Contact):

    @pydantic.validator('home', 'work')
    def is_correct(cls, value):
        return value


class Person(pydantic.BaseModel):
    id: int = random.getrandbits(32)
    name: Name
    mail: Mail
    phone: Phone
