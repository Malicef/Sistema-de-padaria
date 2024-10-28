from src.db import db
from src.view.TelaCadastro import *
from src.view.TelaLogin import *

#essa é a main
def create_db(db):
    db.connect()
    db.create_tables([Funcionario])
    db.create_tables([ItemVenda])
    db.create_tables([Cliente])
    db.create_tables([Produto])
    db.create_tables([Venda])
    db.close()

create_db(db)
print("====== Bem Vindo ======")
print("1. Login")
print("2. Cadastre-se")
print("3. Sair")
entrada = int(input("Escolha: "))

if entrada == 1:
    login = TelaLogin.login()
elif entrada == 2:
    cadastro = TelaCadastro.menuCadastro()
elif entrada == 3:
    print("Saindo...")
    exit()