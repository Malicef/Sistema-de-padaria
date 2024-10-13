from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController

class TelaCadastro:
    def cadastroFuncionario(self):
        print("Cadastro de funcionário:\n")
        nome = str(input("Digite o nome    : "))
        email = str(input("Digite o e-mail  : "))
        senha = str(input("Digite a senha   : "))
        salario = str(input("Digite a salario : "))
        cargo = str(input("Digite o cargo   : "))
        funcionario = FuncionarioController()
        funcionario.cadastrar(nome, email, senha, salario, cargo)

    def cadastroCliente(self):
        print("Cadastro:\n")
        nome = str(input("Digite seu nome   : "))
        email = str(input("Digite seu e-mail : "))
        senha = str(input("Digite sua senha  : "))
        cliente = ClienteController()
        cliente.cadastrar(nome, email, senha) 