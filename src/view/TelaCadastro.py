from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController

class TelaCadastro:
    def menuCadastro():
        print("Cadastra-se como cliente tecle 1, para cadastra-se como funcionario tecle 2")
        cadastro = int(input())
        if cadastro == 1:
            return TelaCadastro.cadastroCliente()
        
        elif cadastro == 2:
            return TelaCadastro.cadastroFuncionario()

    def cadastroFuncionario():
        print("Cadastro de funcionário:\n")
        nome = str(input("Digite o nome    : "))
        email = str(input("Digite o e-mail  : "))
        senha = str(input("Digite a senha   : "))
        salario = str(input("Digite a salario : "))
        cargo = str(input("Digite o cargo   : "))
        funcionario = FuncionarioController()
        funcionario.cadastrarFuncionario(nome, email, senha, salario, cargo)

    def cadastroCliente():
        print("Cadastro:\n")
        nome = str(input("Digite seu nome   : "))
        email = str(input("Digite seu e-mail : "))
        senha = str(input("Digite sua senha  : "))
        cliente = ClienteController()
        cliente.cadastrarCliente(nome, email, senha) 