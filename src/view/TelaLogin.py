from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController
# from src.model.Funcionario import Funcionario
from src.view.TelaCliente import *
from src.view.TelaFuncionario import *

class TelaLogin:
    def login():
        print("==Login==")

        print("Entrar como cliente tecle 1, para entrar como funcionario tecle 2" )
        entrada = int(input())

        email = input("Digite seu email: ")

        senha = input("Digite sua senha: ")

        if entrada == "1":
            cliente = ClienteController.logarCliente(email, senha)
            if cliente != None:
                return TelaCliente.menuCliente(cliente)
            else:
                print("Login ou senha inválidos!")
        elif entrada == "2":
            funcionario = FuncionarioController.loginFuncionario(email, senha)
            if funcionario != None:
                return TelaFuncionario.menuFuncionario(funcionario)
            else:
                print("Login ou senha inválidos!")
