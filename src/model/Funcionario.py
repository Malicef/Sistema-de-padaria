from peewee import CharField
from src.model.Usuario import Usuario

class Funcionario(Usuario):
    cargo = CharField()