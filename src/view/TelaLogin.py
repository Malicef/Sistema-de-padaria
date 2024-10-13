from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController
class TelaLogin:
    def login():
        print("==Login==")

        print("Entrar como cliente tecle 1, para entrar como funcionario tecle 2" )
        entrada = input()

        email = input("Digite seu email: ")

        senha = input("Digite sua senha: ")

        if entrada == "1":
            ClienteController.login(email, senha)
            return ClienteController
        elif entrada == "2":
            logar = FuncionarioController.login(email, senha)
            return logar
