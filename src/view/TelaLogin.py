from src.control.ClienteController import ClienteController
from src.control.FuncionarioController import FuncionarioController
# from src.model.Funcionario import Funcionario
from src.view.TelaCliente import TelaCliente
from src.view.TelaFuncionario import TelaFuncionario

class TelaLogin:
    def login():
        print("==Login==")
        print("Entrar como cliente tecle 1, para entrar como funcionario tecle 2" )

        try:
            entrada = int(input())
            self.menuCliente()

            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            if entrada == 1:
                cliente = ClienteController.logarCliente(email, senha)
                if cliente is not None:
                    return TelaCliente(cliente).menuCliente()
                    print("Login efetuado com sucesso!")
                    print(f"Bem-vindo, {cliente.nome}!")

                else:
                    print("Login ou senha inválidos!")
            elif entrada == 2:
                funcionario = FuncionarioController.loginFuncionario(email, senha)
                if funcionario is not None:
                    return TelaFuncionario.menuFuncionario(funcionario)
                    print("Login efetuado com sucesso!")
                    print(f"Bem-vindo, {funcionario.nome}!")
                else:
                    print("Login ou senha inválidos!")
            else:
                print("Opção inválida! Por favor, digite 1 ou 2.")

        except ValueError:
            print("Por favor, digite um número válido para a opção de login.")
