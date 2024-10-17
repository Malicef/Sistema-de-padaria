
class Carrinho:
    itens: list  = []

    def ValorTotal(self):
        total = 0
        for item in self.itens:
            total += item.valorTotal
        return total