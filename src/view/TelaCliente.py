from src.control.ClienteController import ClienteController
# from src.control.ItemVendaController import ItemVendaController
from src.control.InputController import InputController
from src.model.Cliente import *
from src.control.ItemVendaController import *

class TelaCliente:
    def __init__(self, cliente):
        self.cliente = cliente
        self.carrinho = []

    def menuCliente(self):
        while True:
            print("Login efetuado com sucesso!")
            print(f"Bem-vindo, {self.cliente.nome}!")
            print("\n==Menu Principal==")
            print("1 - Fazer pedido")
            print("2 - Fechar pedido")
            print("3 - Listar compras")
            print("4 - Atualizar conta")
            print("5 - Deletar conta")
            print("6 - Sair")
            opcao = InputController.getInputInteiro(0,6, "Digite a opção desejada")

            if opcao == 1:
                self.fazerPedido()
            elif opcao == 2:
                self.fecharPedido()
            elif opcao == 3:
                ItemVendaController.listarProdutoVenda()
            elif opcao == 4:
                self.atualizarCliente()
            elif opcao == 5:
                self.excluirCliente()
            elif opcao == 6:
                exit("Saindo...")

    def atualizarCliente(self):
        novoNome = input("Digite o novo nome: ")
        novoEmail = input("Digite o novo email: ")
        novaSenha = input("Digite a nova senha: ")
        ClienteController.atualizarCliente(nome=novoNome, email=novoEmail, senha=novaSenha)
        print("Conta atualizada com sucesso!")

    def excluirCliente(self):
        email = input("Digite o email da conta que deseja excluir: ")
        ClienteController.excluirCliente(email)
        print("Conta excluída com sucesso!")

    def fazerPedido(self):
        print("\n== Produtos Disponíveis ==")
        produtos_disponiveis = ProdutoController.listarProdutos()

        if not produtos_disponiveis:
            print("Nenhum produto disponível no momento.")
            return

        while True:
            produto_id = int(input("Digite o ID do produto que deseja adicionar ao carrinho (ou 0 para sair): "))
            if produto_id == 0:
                break

            produto = ProdutoController.buscarProduto(produto_id)
            if not produto:
                print("Produto não encontrado. Tente novamente.")
                continue

            qntd = int(input(f"Digite a quantidade de {produto.nome}: "))
            if qntd > produto.qntdEstoque:
                print(f"Quantidade indisponível. Estoque atual: {produto.qntdEstoque}.")
                continue

            # Adiciona produto ao carrinho
            self.carrinho.append((produto, qntd))
            print(f"{qntd} unidades de {produto.nome} adicionadas ao carrinho.")

    def fecharPedido(self):
        if not self.carrinho:
            print("Carrinho vazio. Adicione produtos antes de fechar o pedido.")
            return

        print("\n== Fechando Pedido ==")
        funcionario_id = int(input("Digite o ID do funcionário responsável pelo pedido: "))

        try:
            venda = VendaController.criarVenda(funcionario_id, self.cliente, None)

            # Adiciona os itens da venda
            for produto, qntd in self.carrinho:
                ItemVendaController.criarItemVenda(produto, venda, qntd)

                # Atualiza o estoque do produto
                novo_estoque = produto.qntdEstoque - qntd
                ProdutoController.atualizarProduto(
                    produto.id, produto.nome, produto.preco, novo_estoque,
                    produto.categoria, produto.descricao
                )

            print("Pedido fechado com sucesso!")
            self.carrinho.clear()

        except Exception as e:
            print(f"Erro ao fechar pedido: {e}")