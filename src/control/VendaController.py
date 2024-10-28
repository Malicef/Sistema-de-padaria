from src.model.Venda import Venda
from src.model.Produto import Produto

class VendaController():
    @staticmethod
    def criarVenda(funcionario, cliente, produto):
        try:
            print(funcionario, cliente, produto)
            venda = Venda.create(funcionario=funcionario, cliente=cliente, produto=produto)
            return venda
        except Exception as e:
            return False, str(e)

    @staticmethod
    def listarVenda():
        try:
            venda = Venda.select()
            return[
                print({
                    "id": venda.id,
                    "funcionario": venda.funcionario.nome,
                    "cliente": venda.cliente.nome,
                    "produto": venda.produto.nome
                })
            for venda in venda
            ]
        except Exception as e:
            return False, str(e)

    @staticmethod
    def buscarVenda(venda_id):
        try:
            venda = Venda.get(Venda_id == venda_id)
            return venda
        except Exception as e:
            return False, str(e)
