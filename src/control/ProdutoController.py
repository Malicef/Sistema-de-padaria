from src.model.Produto import Produto

class ProdutoController:

    @staticmethod
    def adicionarProduto(nome, preco, qntdEstoque, categoria, descricao):
        try:
            produto = Produto.create(nome=nome, preco=preco, qntdEstoque=qntdEstoque, categoria=categoria, descricao=descricao)
            print("Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def listarProdutoID(produto_id):
        try:
            produto = Produto.get(Produto.id == produto_id)
            print({
                'Id': produto.id,
                'Nome': produto.nome,
                'Preço': produto.preco,
                'Quantidade': produto.qntdEstoque,
                'Categoria': produto.categoria,
                'Descrição': produto.descricao,
            })
        except Produto.DoesNotExist:
            print('Produto não encontrado!')
        except Exception as e:
            print(f"Erro: {e}")

    @staticmethod
    def listarProdutos():
        try:
            produtos = Produto.select()
            return [
                print({
                    'Id': produto.id,
                    'Nome': produto.nome,
                    'Preço': produto.preco,
                    'Quantidade': produto.qntdEstoque,
                    'Categoria': produto.categoria,
                    'Descrição': produto.descricao,
                })
                for produto in produtos
            ]
        except Exception as e:
            return str(e)

    @staticmethod
    def atualizarProduto( id, nome, preco, qntdEstoque, categoria, descricao):
        try:
            produto = Produto.get(Produto.id == id)
            produto.nome = nome
            produto.preco = preco
            produto.qntdEstoque = qntdEstoque
            produto.categoria = categoria
            produto.descricao = descricao
            produto.save()
            return True, f'Produto "{nome}" atualizado com sucesso!'
        except Produto.DoesNotExist:
            return False, f'Produto "{nome}" não encontrado!'
        except Exception as e:
            return False, str(e)

    @staticmethod
    def excluirProduto(id):
        try:
            produto = Produto.get(Produto.id == id)
            produto.delete_instance()
            return True, 'Produto excluído com sucesso!'
        except Produto.DoesNotExist:
            return False, 'Produto não encontrado!'
        except Exception as e:
            return False, str(e)