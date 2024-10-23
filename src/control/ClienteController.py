from src.model.Cliente import Cliente

class ClienteController(Cliente):
    @staticmethod
    def cadastrarCliente(nome, email, senha):
        try:
            cliente = Cliente.create(nome=nome, senha=senha, email=email)
            return True, "Cliente cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)
    @staticmethod
    def logarCliente(email, senha):
        try:
            cliente = Cliente.get(Cliente.email == email)
            if cliente.senha == senha:
                return cliente
            else:
                return None
        except Cliente.DoesNotExist:
            return None
    @staticmethod
    def listarClientes():
        try:
            cliente = Cliente.select()
            return[
                print({
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "email": cliente.email
                })
                for cliente in cliente 
            ]
        except Exception as e:
            return str(e)
    @staticmethod
    def atualizarCliente(nome, senha, email):
        try:
            cliente = Cliente.get(Cliente.email == email)
            cliente.nome = nome
            cliente.senha = senha 
            cliente.email = email
            cliente.save()
        except Cliente.DoesNotExist:
            return False, "Cliente não encontrado."
        except Exception as e:
            return False, str(e)
    @staticmethod
    def excluirCliente(email):
        try:
            Cliente.delete().where(Cliente.email == email).execute()
            return True, "Cliente deletado com sucesso!"
        except Exception as e:
            return False, str(e)