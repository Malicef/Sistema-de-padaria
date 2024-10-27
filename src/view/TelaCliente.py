from src.control.ClienteController import ClienteController
# from src.control.ItemVendaController import ItemVendaController
from src.control.InputController import InputController
from src.model.Cliente import *
from src.control.ItemVendaController import *

class TelaCliente:
    def menuCliente(cliente : Cliente):
        print("Login efetuado com sucesso!")
        print(f"Bem-vindo, {cliente.nome}!")
        print("\n==Menu Principal==")
        print("1 - Adicionar ao carrinho")
        print("2 - Fazer pedido")
        print("3 - Fechar pedido")
        print("4 - Listar compras")
        print("5 - Deletar conta")
        print("6 - Atualizar conta")
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
            ClienteController.atualizarCliente()
        elif opcao == 5:
            ClienteController.excluirCliente()
        elif opcao == 6:
            ItemVendaController.listarProdutoVenda()
        elif opcao == 7:
            print("Saindo...")
            return 

    def atualizarCliente():
        novoNome = input("Digite o novo nome: ")
        novoEmail = input("Digite o novo email: ")
        novaSenha = input("Digite a nova senha: ")
        ClienteController.atualizarCliente(nome=novoNome, email=novoEmail, senha=novaSenha)
        print("Conta atualizada com sucesso!")

    def excluirCliente():
        email = input("Digite o email da conta que deseja excluir: ")
        ClienteController.excluirCliente(email)
        print("Conta excluída com sucesso!")