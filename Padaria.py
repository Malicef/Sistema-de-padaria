from src.db import db
from src.model.Venda import Venda
from src.model.Usuario import Usuario
from src.model.Cliente import Cliente
from src.model.Produto import Produto
from src.model.ItemVenda import ItemVenda
from src.model.Funcionario import Funcionario
from src.control.VendaController import VendaController
from src.control.ProdutoController import ProdutoController
from src.control.FuncionarioController import FuncionarioController


#essa é a main
def create_db(db):
    db.connect()
    db.create_tables([Funcionario])
    db.create_tables([ItemVenda])
    db.create_tables([Usuario])
    db.create_tables([Cliente])
    db.create_tables([Produto])
    db.create_tables([Venda])
    db.close()

create_db(db)

'''
# main template

option = input("insira o comando: ")

while True:
    match option:
        case "sair":
            exit()

        case "funcionario":
            ...
        case "cliente":
            ...
        case "produto":
            ...
        case "venda":
            ...
        case "usuario":
            ...
        case _:
            print("Opção Invalida! Tente novamente")
'''