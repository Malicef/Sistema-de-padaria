from peewee import Model, CharField, IntegerField, FloatField
from src.db import BaseModel

class Produto(BaseModel):
    __nome = CharField(max_length=100)
    __preco = FloatField()
    __qntdEstoque = IntegerField()
    __categoria = CharField(max_length=100)
    __descricao = CharField(max_length=100)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("Preço inválido. O preço não pode ser negativo.")
        self.__preco = preco

    @property
    def qntdEstoque(self):
        return self.__qntdEstoque
    
    @qntdEstoque.setter
    def qntdEstoque(self, qntdEstoque):
        if qntdEstoque < 0:
            raise ValueError("Quantidade inválida. A quantidade não pode ser negativa.")
        self.__qntdEstoque = qntdEstoque

    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao