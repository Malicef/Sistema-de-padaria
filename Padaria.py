from src.db import db
from src.model.Usuario import Usuario
from src.model.Cliente import Cliente
from src.model.Funcionario import Funcionario
from src.model.Venda import Venda
from src.model.Produto import Produto
from src.model.ItemVenda import ItemVenda
from src.control.FuncionarioController import FuncionarioController

#essa é a main
def create_db(db):
    db.connect()
    db.create_tables([Cliente])
    db.create_tables([Funcionario])
    db.create_tables([Venda])
    db.create_tables([Produto])
    db.create_tables([ItemVenda])
    db.close()

create_db(db)

# FuncionarioController.cadastrar("Pedro", "Pedro@gmail.com", "123", 2000, "Padeiro")
# FuncionarioController.listar()
# FuncionarioController.login('Pedro@gmail.com', '123')
    
