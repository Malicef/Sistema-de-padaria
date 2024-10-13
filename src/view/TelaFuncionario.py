from src.model.Funcionario import *
from src.control.FuncionarioController import *
from src.control.ProdutoController import *
from src.control.ClienteController import *
from src.control.VendaController import *
from src.control.InputController import InputController

class TelaFuncionario:
    def menuFuncionario(funcionario: Funcionario):
        print("Login efetuado com sucesso!")
        print(f"Bem-vindo, {funcionario.nome}!")
        print("\n==Menu Principal==")
        print("1 - Cadastrar Produto")
        print("2 - Cadastrar Cliente")
        print("3 - Cadastrar Funcionário")
        print("4 - Listar Produtos")
        print("5 - Listar Clientes")
        print("6 - Excluir Cliente")
        print("7 - Listar Funcionários")
        print("8 - Excluir Funcionario")
        print("9 - Realizar Venda")
        print("10 - Listar venda")
        print("11 - Excluir venda")
        print("12 - Sair")
        opcao = InputController.getInputInteiro(0,12, "Digite a opção desejada")

        if opcao == 1:
            TelaFuncionario.cadastrarProduto(funcionario)
        elif opcao == 2:
            TelaFuncionario.cadastrarCliente(funcionario)
        elif opcao == 3:
            TelaFuncionario.cadastrarFuncionario(funcionario)
        elif opcao == 4:
            TelaFuncionario.listarProdutos()
        elif opcao == 5:
            TelaFuncionario.listarClientes()
        elif opcao == 6:
            TelaFuncionario.excluirCliente()
        elif opcao == 7:
            TelaFuncionario.listarFuncionarios()
        elif opcao == 8:
            TelaFuncionario.excluirFuncionario()
        elif opcao == 9:
            TelaFuncionario.realizarVenda(funcionario)
        elif opcao == 10:
            TelaFuncionario.listarVenda()
        elif opcao == 11:
            TelaFuncionario.excluirVenda(funcionario)
        elif opcao == 12:
            print("Saindo...")
            return 

    @staticmethod
    def cadastrarProduto(funcionario):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        qntdEstoque = int(input("Digite a quantidade em estoque do produto: "))
        categoria = input("Digite a categoria do produto: ")
        descricao = input("Digite a descrição do produto: ")
        ProdutoController.adicionarProduto(nome, preco, qntdEstoque, categoria, descricao)
        print("Produto cadastrado com sucesso!")
    