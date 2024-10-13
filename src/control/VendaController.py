from src.model.Venda import Venda
from src.model.Produto import Produto

class VendaController(Venda):
    def __init__(self):
        #self.cliente = cliente
        self.itens = []
        self.total = 0

    def adicionarProduto(self, id, quantidade):
        try:
            produto = Produto.get(Produto.id == id)
            if quantidade <= produto.qntdEstoque:
                produto.qntdEstoque -= quantidade
                produto.save()

                self.itens.append((produto.nome, quantidade))
                self.total += produto.preco * quantidade

                print("Produto foi adicionado!")
                print(f"Total de itens: {self.itens}")
                print(f"Total: R$ {self.total:.2f}")
                self.produtoCliente = produto
            else:
                print(f"Estoque insuficiente para {produto.nome}.")
        except Produto.DoesNotExist:
            print(f"Produto com ID {id} não encontrado.")

    def fecharVenda(self):
        #print(f"Carrinho de {cliente.nome}")
        for produto, quantidade in self.itens:
            print(f"{produto.nome} - {quantidade} unidade(s) - R$ {produto.preco * quantidade:.2f}")
        print(f"Total: R$ {self.total:.2f}")