from peewee import ForeignKeyField, IntegerField
from src.model.Cliente import Cliente
from src.model.Produto import Produto
from src.model.Funcionario import Funcionario
from src.db import BaseModel

class Venda(BaseModel):
    funcionario = ForeignKeyField(Funcionario, backref= "venda" )
    cliente = ForeignKeyField(Cliente, backref= "venda" )
    produto = ForeignKeyField(Produto, backref="venda")
