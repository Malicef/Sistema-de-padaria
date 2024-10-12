from peewee import ForeignKeyField, IntegerField
from src.db import BaseModel
from src.model.Produto import Produto
from src.model.Venda import Venda


class ItemVenda(BaseModel):
    __produto = ForeignKeyField(Produto, backref= "itemVenda" )
    __venda = ForeignKeyField(Venda, backref= "itemVenda" )
    __qntdItem = IntegerField()

    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    @property
    def venda(self):
        return self.__venda
    
    @venda.setter
    def venda(self, venda):
        self.__venda = venda
    
    @property
    def qntdItem(self):
        return self.__qntdItem
    
    @qntdItem.setter
    def qntdItem(self, qntdItem):
        self.__qntdItem = qntdItem
        
  