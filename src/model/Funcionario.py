from peewee import CharField, DecimalField
from src.model.Usuario import Usuario

class Funcionario(Usuario):
    __cargo = CharField()
    __salario = DecimalField()

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario