from src.model.Venda import Venda
from src.model.Produto import Produto

class VendaController():
    def criarVenda(funcionario, cliente, produto):
        if not Produto.get_by_id(produto):
            return False, "Produto não encontrado."
        venda = Venda.create(funcionario, cliente, produto)
        return True, "Venda bem sucedida!"
    
    def cancelarVenda(venda_id):
        venda = Venda.get_by_id(venda_id)
        if not venda:
            return False, "Venda não encontrada."
        venda.delete_instance()
        return True, "Venda cancelada com sucesso!"
    
    def listarVendas():
        vendas = Venda.select()
        vendas_list = []
        for venda in vendas:
            vendas_list.append({
                "id": venda.id,
                "funcionario": venda.funcionario.nome,
                "cliente": venda.cliente.nome,
                "produto": venda.produto.nome
            })
        return vendas_list
    
    def buscarVenda(venda_id):
        venda = Venda.get_by_id(venda_id)
        if not venda:
            return False, "Venda não encontrada."
        return True, {
            "id": venda.id,
            "funcionario": venda.funcionario.nome,
            "cliente": venda.cliente.nome,
            "produto": venda.produto.nome
        }

    