from src.model.ItemVenda import ItemVenda
from src.control.ProdutoController import ProdutoController

class ItemVendaController:
    @staticmethod
    def criarItemVenda(produto, venda, qntdItem):
        valor = qntdItem * produto.preco
        item = ItemVenda.create(produto, venda, qntdItem, valor)
        return item
    
    @staticmethod
    def listarProdutoVenda():
        i = ItemVenda.select()
        for item in i:
            print(f"ID: {item.id}, Produto: {item.produto.nome}, Quantidade: {item.qntdItem}")
            ProdutoController.listarProdutoID(item.produto.id)
            print("Preco total: " )