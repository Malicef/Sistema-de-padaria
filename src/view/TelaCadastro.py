from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController
from src.view.TelaCliente import *
from src.view.TelaFuncionario import *

class TelaCadastro:
    def menuCadastro():
        print("Cadastra-se como cliente tecle 1")
        print("Cadastra-se como funcionario tecle 2")
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
        cargo = str(input("Digite o cargo   : "))
        funcionario = FuncionarioController()
        funcionario.cadastrarFuncionario(nome, email, senha, cargo)
        if funcionario:
            user = FuncionarioController.loginFuncionario(email, senha)
            return TelaFuncionario.menuFuncionario(user)
        else:
            print("Erro ao cadastrar o funcionário.")

    def cadastroCliente():
        print("Cadastro:\n")
        nome = str(input("Digite seu nome   : "))
        email = str(input("Digite seu e-mail : "))
        senha = str(input("Digite sua senha  : "))
        cliente = ClienteController()
        cliente.cadastrarCliente(nome, email, senha) 
        user = cliente.logarCliente(email, senha)
        if user:
            return TelaCliente.menuCliente(user)
        else:
            print("Erro ao cadastrar o cliente.")