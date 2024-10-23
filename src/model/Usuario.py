from peewee import CharField
from src.db import BaseModel

class Usuario(BaseModel):
    nome = CharField(max_length=100)
    email = CharField(unique=True)
    senha = CharField()
