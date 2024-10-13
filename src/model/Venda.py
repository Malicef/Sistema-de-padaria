from peewee import ForeignKeyField, IntegerField
from src.model.Cliente import Cliente
from src.model.Produto import Produto
from src.model.Funcionario import Funcionario
from src.db import BaseModel

class Venda(BaseModel):
    __funcionario = ForeignKeyField(Funcionario, backref= "venda" )
    __cliente = ForeignKeyField(Cliente, backref= "venda" )
    __produto = ForeignKeyField(Produto, backref="venda")

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto