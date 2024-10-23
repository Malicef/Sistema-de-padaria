from peewee import CharField, IntegerField, FloatField
from src.db import BaseModel

class Produto(BaseModel):
    nome = CharField(max_length=100)
    preco = FloatField()
    qntdEstoque = IntegerField()
    categoria = CharField(max_length=100)
    descricao = CharField(max_length=100)
