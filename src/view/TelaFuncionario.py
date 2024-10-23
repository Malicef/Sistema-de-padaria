from src.model.Funcionario import *
from src.control.FuncionarioController import *
from src.control.ProdutoController import *
from src.control.ClienteController import *
from src.control.VendaController import *
from src.control.InputController import InputController
# from src.view import TelaLogin
from src.view.TelaCadastro import *

class TelaFuncionario:

    def menuFuncionario(funcionario: Funcionario):
        print("Login efetuado com sucesso!")
        print(f"Bem-vindo, {funcionario.nome}!")
        print("\n==Menu Principal==")
        print("1 - Cadastrar Produto")
        # print("2 - Cadastrar Cliente")
        # print("3 - Cadastrar Funcionário")
        print("4 - Listar Produtos")
        print("5 - Listar Clientes")
        # print("6 - Excluir Cliente")
        print("7 - Listar Funcionários")
        # print("8 - Excluir Funcionario")
        print("9 - Realizar Venda")
        print("10 - Listar venda")
        print("11 - Excluir venda")
        print("12 - Buscar venda")
        print("13 - Sair")
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
            TelaFuncionario.criarVenda(funcionario)
        elif opcao == 10:
            TelaFuncionario.listarVenda()
        elif opcao == 11:
            TelaFuncionario.cancelarVenda(funcionario)
        elif opcao == 12:
            TelaFuncionario.buscarVenda(funcionario)
        elif opcao == 13:
            print("Saindo...")
            exit()
            return 

    @staticmethod
    def cadastrarProduto(Produto):
        qntd = int(input("Deseja cadastrar quantos produtos? "))
        for i in range(qntd):
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            qntdEstoque = int(input("Digite a quantidade em estoque do produto: "))
            categoria = input("Digite a categoria do produto: ")
            descricao = input("Digite a descrição do produto: ")
            ProdutoController.adicionarProduto(nome, preco, qntdEstoque, categoria, descricao)
            print("Produto cadastrado com sucesso!")

    def cadastrarCliente(funcionario):
        nome = input("Digite o nome do Cliente: ")
        email = input("Digite o email do Cliente")
        senha = input("Digite a senha do cliente")
        ClienteController.cadastrarCliente(nome, email, senha)
        print("Cliente cadastrado com sucesso!")

    def cadastrarFuncionario(funcionario):
        nome = input("Digite o nome do Funcionario: ")
        email = input("Digite o email do Funcionario")
        senha = input("Digite a senha do Funcionario")
        cargo = input("Digite o cargo do Funcionario")
        salario = input("Digite o salario do Funcionario")
        FuncionarioController.cadastrarFuncionario(nome, email, senha, salario, cargo)
        print("Funcionario cadastrado com sucesso!")

    def listarProdutos():
        return ProdutoController.listarProdutos()

    def listarClientes():
        return ClienteController.listarClientes()

    def excluirCliente(email):
        email = input("Digite o email da conta que deseja excluir: ")
        ClienteController.excluirCliente(email)
        print("Conta excluída com sucesso!")

    def listarFuncionarios():
        return FuncionarioController.listarFuncionarios()

    def excluirFuncionario(email):
        email = input("Digite o email do Funcionario que deseja excluir: ")
        FuncionarioController.excluirFuncionario(email)
        print("Funcionario excluído com sucesso!")

    def criarVenda():
        pass

    def listarVenda():
        return VendaController.listarVenda()

    def buscarVenda():
        pass

    def cancelarVenda():
        pass