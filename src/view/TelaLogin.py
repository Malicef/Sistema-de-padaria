from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController
from src.view.TelaCliente import TelaCliente
from src.view.TelaFuncionario import TelaFuncionario

class TelaLogin:
    @staticmethod
    def factory_tela(tela: int):
        if tela == 1:
            return TelaCliente
        if tela == 2:
            return TelaFuncionario
        else:
            print("Saindo...")
    
    @staticmethod
    def factory_login(user: int):
        if user == 1:
            return ClienteController
        if user == 2:
            return FuncionarioController
        else:
            print('Saindo...')


    def login():
        print("==Login==")
        print("Entrar como cliente tecle 1, para entrar como funcionario tecle 2" )

        try:
            entrada = int(input())
            tela = TelaLogin.factory_tela(entrada)

            user = TelaLogin.factory_login(entrada)

            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            
            user = user.login(email, senha)
            if user is not None:
                print("\n\nLogin efetuado com sucesso!")
                print(f"Bem-vindo, {user.nome}!")
                return tela.menu(user)

            else:
                print("Login ou senha inválidos!")


        except ValueError:
            print("Por favor, digite um número válido para a opção de login.")
