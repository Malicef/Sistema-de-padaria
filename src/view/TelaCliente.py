from src.control.ClienteController import ClienteController
# from src.control.ItemVendaController import ItemVendaController
from src.control.InputController import InputController
from src.model.Cliente import *
from src.model.Funcionario import *
from src.control.ItemVendaController import *

carrinho = []

class TelaCliente:

    def menu (cliente):
        while True:
            print("\n==Menu Principal==")
            print("1 - Adicionar ao carrinho")
            print("2 - Fechar pedido")
            print("3 - Listar compras")
            print("4 - Atualizar conta")
            print("5 - Deletar conta")
            print("6 - Sair")
            opcao = InputController.getInputInteiro(0,6, "Digite a opção desejada")

            if opcao == 1:
                TelaCliente.fazerPedido(cliente)
            elif opcao == 2:
                TelaCliente.fecharPedido(cliente)
            elif opcao == 3:
                ItemVendaController.listarProdutoVenda(cliente)
            elif opcao == 4:
                TelaCliente.atualizarCliente(cliente)
            elif opcao == 5:
                TelaCliente.excluirCliente(cliente)
                exit("Saindo...")
            elif opcao == 6:
                exit("Saindo...")

    def atualizarCliente(cliente):
        novoNome = input("Digite o novo nome: ")
        novoEmail = input("Digite o novo email: ")
        novaSenha = input("Digite a nova senha: ")
        ClienteController.atualizarCliente(cliente ,nome=novoNome, email=novoEmail, senha=novaSenha)
        print("Conta atualizada com sucesso!")

    def excluirCliente(cliente):
        email = input("Digite o email da conta que deseja excluir: ")
        ClienteController.excluirCliente(email)
        print("Conta excluída com sucesso!")

    def fazerPedido(cliente):
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
            dict_item = {'produto' : produto,
                        'qntd' : qntd
                        }

            carrinho.append(dict_item)
            print(f"{qntd} unidades de {produto.nome} adicionadas ao carrinho.")

    def fecharPedido(cliente):
        if not carrinho:
            print("Carrinho vazio. Adicione produtos antes de fechar o pedido.")
            return

        funcionario = Funcionario.get_or_create(nome='Loja Virtual', email='padaria@gmail.com', senha='padaria', cargo='store')
        

        print("\n== Fechando Pedido ==")

        try:
            # Cria a venda e os itens da venda
            for item in carrinho:
                produto = item['produto']
                qntd = item['qntd']
                VendaController.criarVenda(cliente, funcionario[0], produto)
                venda = Venda.get_or_create(cliente=cliente, funcionario=funcionario[0], produto=produto)
                ItemVendaController.criarItemVenda(produto, venda[0], qntd)
                print(f"{qntd} unidades de {produto.nome} adicionadas ao pedido.")

            # Atualiza o estoque do produto
                novo_estoque = produto.qntdEstoque - qntd
                ProdutoController.atualizarProduto(
                    produto.id, produto.nome, produto.preco, novo_estoque,
                    produto.categoria, produto.descricao
                )

            print("Pedido fechado com sucesso!")
            carrinho.clear()

        except Exception as e:
            print(f"Erro ao fechar pedido: {e}")