from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

Config.set('graphics', 'fullscreen', '0')

class HomeScreen(Screen):
    pass
class EscolherLogin(Screen):
    pass
class EscolherCadastro(Screen):
    pass

class CadastrarCliente(Screen):
    pass
class LoginCliente(Screen):
    pass

class CadastrarFuncionario(Screen):
    pass
class LoginFuncionario(Screen):
    pass


class Interface(App):
    def build(self):
        self.title = "Padaria - Python"
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(EscolherLogin(name='escolherLogin'))
        sm.add_widget(EscolherCadastro(name='escolherCadastro'))

        sm.add_widget(CadastrarCliente(name='cadastrarCliente'))
        sm.add_widget(LoginCliente(name='loginCliente'))
        #sm.add_widget(ListarClientes(name='listarClientes'))
        #sm.add_widget(AtualizarCliente(name='atualizarCliente'))
        #sm.add_widget(DeletarCliente(name='deletarCliente'))

        sm.add_widget(LoginFuncionario(name='loginFuncionario'))
        sm.add_widget(CadastrarFuncionario(name='cadastrarFuncionario'))
        #sm.add_widget(ListarFuncionario(name='listarFuncionario'))
        #sm.add_widget(AtualizarFuncionario(name='atualizarFuncionario'))
        #sm.add_widget(DeletarFuncionario(name='deletarFuncionario'))

        #sm.add_widget(CriarItemVenda(name='criarItemVenda'))
        #sm.add_widget(ListarProdutoVenda(name='listarItemVenda'))

        #sm.add_widget(AdicionarProdutoVenda(name='adicionarProdutoVenda'))
        #sm.add_widget(listarProdutoIdProdutoVenda(name=listarProdutoIdProtutoVenda'))
        #sm.add_widget(listarProdutosProdutoProdutoVenda(name='listarProdutosProdutoVenda'))
        #sm.add_widget(AtualizarProdutoProdutoVenda(name='atualizarProdutoProdutoVenda'))
        #sm.add_widget(ExcluirProduto(ProdutoVenda(name='excluirProdutoProdutoVenda'))
        return sm

    def sairDoApp(self):
        exit()

if __name__ == '__main__':
    Interface().run()