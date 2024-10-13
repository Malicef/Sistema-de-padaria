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
from src.control.VendaController import VendaController


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

print("==Login==")

login = input("Digite seu login: ")

senha = input("Digite sua senha: ")

funcionario_controller = FuncionarioController()

funcionario = funcionario_controller.login(login, senha)

if funcionario:
    print("Login efetuado com sucesso!")
    print(f"Bem-vindo, {funcionario.nome}!")
    print("\n==Menu Principal==")
    print("1 - Cadastrar Produto")
    print("2 - Cadastrar Cliente")
    print("3 - Cadastrar Funcionário")
    print("4 - Cadastrar Usuário")
    print("5 - Listar Produtos")
    print("6 - Listar Clientes")
    print("7 - Listar Funcionários")
    print("8 - Listar Usuários")
    print("9 - Realizar Venda")
    print("10 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    
    while opcao != 10:
    
        if opcao == 1: 
            print("\n==Cadastrar Produto==")
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            qntdEstoque = int(input("Quantidade em estoque: "))
            categoria = input("Categoria do produto: ")
            descricao = input("Descrição do produto: ")
            produto_controller = ProdutoController()
            produto_controller.cadastrar(nome, preco, qntdEstoque, categoria, descricao)
            print("Produto cadastrado com sucesso!")

            