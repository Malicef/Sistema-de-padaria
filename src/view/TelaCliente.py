from src.control.ClienteController import ClienteController
from src.control.ItemVendaController import ItemVendaController
from src.control.InputController import InputController

class TelaCliente:
    def menuCliente(cliente : Cliente):
        print("Login efetuado com sucesso!")
        print(f"Bem-vindo, {cliente.nome}!")
        print("\n==Menu Principal==")
        print("1 - Adicionar ao carrinho")
        print("2 - Ver items no carrinho")
        print("3 - Fechar pedido")
        print("4 - Atualizar conta")
        print("5 - Deletar conta")
        print("6 - Sair")
        opcao = InputController.getInputInteiro(0,6, "Digite a opção desejada")

        if opcao == 1:
            #ItemVendaController.adicionarAoCarrinho()
            ...
        elif opcao == 2:
            #ItemVendaController.listarCarrinho()
            ...
        elif opcao == 3:
            #ItemVendaController.fecharPedido()
            ...
        elif opcao == 4:
            ClienteController.atualizar(nome, senha, email)
        elif opcao == 5:
            ClienteController.deletar(email)
        elif opcao == 6:
            print("Saindo...")
            return 