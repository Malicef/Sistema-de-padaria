from peewee import ForeignKeyField, IntegerField, FloatField
from src.db import BaseModel
from src.model.Produto import Produto
from src.model.Venda import Venda


class ItemVenda(BaseModel):
    produto = ForeignKeyField(Produto, backref= "itemVenda" )
    venda = ForeignKeyField(Venda, backref= "itemVenda" )
    qntdItem = IntegerField()
    valorTotal = FloatField()
