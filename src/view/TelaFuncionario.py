from src.model.Funcionario import *
from src.control.FuncionarioController import *
from src.control.ProdutoController import *
from src.control.ClienteController import *
from src.control.VendaController import *
from src.control.InputController import InputController
from src.view.TelaCadastro import *

class TelaFuncionario:
    def menuFuncionario(funcionario : Funcionario):
        while True:
            print("Login efetuado com sucesso!")
            print(f"Bem-vindo, {funcionario.nome}!")
            print("\n==Menu Principal==")
            print("1 - Cadastrar Produto")
            print("2 - Cadastrar Cliente")
            print("3 - Cadastrar Funcionário")
            print("4 - Listar Produtos")
            print("5 - Listar Clientes")
            print("6 - Excluir Cliente")
            print("7 - Listar Funcionários")
            print("8 - Excluir Funcionario")
            print("9 - Realizar Venda")
            print("10 - Listar venda")
            print("11 - Buscar venda")
            print("12 - Sair")
            opcao = InputController.getInputInteiro(0,13, "Digite a opção desejada")

            if opcao == 1:
                TelaFuncionario.cadastrarProduto(funcionario)
            elif opcao == 2:
                TelaFuncionario.cadastrarCliente(funcionario)
            elif opcao == 3:
                TelaFuncionario.cadastrarFuncionario(funcionario)
            elif opcao == 4:
                TelaFuncionario.listarProdutos()
            elif opcao == 5:
                TelaFuncionario.listarClientes()
            elif opcao == 6:
                TelaFuncionario.excluirCliente(funcionario)
            elif opcao == 7:
                TelaFuncionario.listarFuncionarios()
            elif opcao == 8:
                TelaFuncionario.excluirFuncionario(funcionario)
            elif opcao == 9:
                TelaFuncionario.criarVenda(funcionario)
            elif opcao == 10:
                TelaFuncionario.listarVenda()
            elif opcao == 11:
                TelaFuncionario.buscarVenda(funcionario)
            elif opcao == 12:
                print("Saindo...")
            

    @staticmethod
    def cadastrarProduto(funcionario):
        qntd = int(input("Deseja cadastrar quantos produtos? "))
        for i in range(qntd):
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            qntdEstoque = int(input("Digite a quantidade em estoque do produto: "))
            categoria = input("Digite a categoria do produto: ")
            descricao = input("Digite a descrição do produto: ")
            ProdutoController.adicionarProduto(nome, preco, qntdEstoque, categoria, descricao)
            print("Produto cadastrado com sucesso!")
        input("Pressione Enter para voltar ao menu...")  
     
    @staticmethod
    def cadastrarCliente(funcionario):
        nome = input("Digite o nome do Cliente: ")
        email = input("Digite o email do Cliente: ")
        senha = input("Digite a senha do cliente: ")
        ClienteController.cadastrarCliente(nome, email, senha)
        print("Cliente cadastrado com sucesso!")
        input("Pressione Enter para voltar ao menu...")  

    @staticmethod
    def cadastrarFuncionario(funcionario):
        nome = input("Digite o nome do Funcionario: ")
        email = input("Digite o email do Funcionario: ")
        senha = input("Digite a senha do Funcionario: ")
        cargo = input("Digite o cargo do Funcionario: ")
        FuncionarioController.cadastrarFuncionario(nome, email, senha, cargo)
        print("Funcionario cadastrado com sucesso!")
        input("Pressione Enter para voltar ao menu...")  
    
    @staticmethod
    def listarProdutos():
        ProdutoController.listarProdutos() 
        input("Pressione Enter para voltar ao menu...")    

    @staticmethod
    def listarClientes():
        ClienteController.listarClientes()
        input("Pressione Enter para voltar ao menu...")  

    @staticmethod
    def excluirCliente(email):
        email = input("Digite o email da conta que deseja excluir: ")
        ClienteController.excluirCliente(email)
        print("Conta excluída com sucesso!")
        input("Pressione Enter para voltar ao menu...")  

    @staticmethod
    def listarFuncionarios():
        FuncionarioController.listarFuncionarios()
        input("Pressione Enter para voltar ao menu...")  

    @staticmethod
    def excluirFuncionario(email):
        email = input("Digite o email do Funcionario que deseja excluir: ")
        FuncionarioController.excluirFuncionario(email)
        print("Funcionario excluído com sucesso!")
        input("Pressione Enter para voltar ao menu...")  

    @staticmethod
    def criarVenda(funcionario):
        ClienteController.listarClientes()
        id_cliente = int(input("Informe o ID do cliente: "))
        cliente_buscado = ClienteController.buscarCliente(id_cliente)

        if(ProdutoController.listarProdutos() == False):
            return print("Nenhum produto cadastrado")

        idProduto = int(input("Informe o ID do produto: "))
        produtoBuscado = ProdutoController.buscarProduto(idProduto)
        
        nova_venda = VendaController.criarVenda(funcionario, cliente_buscado, produtoBuscado)

        qntd = int(input("Informe a quantidade do produto: "))


        if (qntd > produtoBuscado.qntdEstoque):
            print("Quantidade informada não existe em estoque!")
            return 

        ItemVendaController.criarItemVenda(produtoBuscado, nova_venda, qntd)
        produtoBuscado.qntdEstoque -= qntd
        ProdutoController.atualizarProduto(produtoBuscado.id, produtoBuscado.nome, produtoBuscado.preco, produtoBuscado.qntdEstoque, produtoBuscado.categoria, produtoBuscado.descricao)
        print ("Venda realizada!")

        input("Pressione Enter para voltar ao menu...")  

    def listarVenda():
        VendaController.listarVenda()
        input("Pressione Enter para voltar ao menu...")  

    def buscarVenda(venda_id):
        VendaController.listarVenda()
        IDvenda =  int(input("Digite o ID da venda que deseja buscar: "))
        venda = VendaController.buscarVenda(IDvenda)
        item = ItemVendaController.listarItemVendaId(IDvenda)
        input("Pressione Enter para voltar ao menu...")  

