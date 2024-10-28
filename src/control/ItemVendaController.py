from src.model.ItemVenda import ItemVenda
from src.control.ProdutoController import ProdutoController
from src.control.VendaController import *

class ItemVendaController:
    @staticmethod
    def criarItemVenda(produto, venda, qntdItem):
        valor = qntdItem * produto.preco
        item = ItemVenda.create(produto=produto, venda=venda, qntdItem=qntdItem, valorTotal=valor)
        return item
    
    @staticmethod
    def listarProdutoVenda():
        i = ItemVenda.select()
        for item in i:
            print(f"ID: {item.id}, Produto: {item.produto.nome}, Quantidade: {item.qntdItem}")
            ProdutoController.listarProdutoID(item.produto.id)
            print("Preco total: " )

    def listarItemVendaId(id_venda):
        try:
            print(id_venda)
            vendas = ItemVenda.select()

            for v in vendas:
                if v.venda.id == id_venda:
                    print(f'Produto: {v.produto.nome}')
                    print(f'Quantidade: {v.qntdItem}')
                    print(f'Valor: R${v.valorTotal}')
                    return

        except Venda.DoesNotExist:
            print("Venda não encontrada.")