from peewee import CharField
from src.db import BaseModel

class Usuario(BaseModel):
    __nome = CharField(max_length=100)
    __email = CharField(unique=True)
    __senha = CharField()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        self.__senha = value