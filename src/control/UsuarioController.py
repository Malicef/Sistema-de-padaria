from src.model.Usuario import Usuario

class UsuarioController():

    def cadastrar(self, nome, email, senha):
        try:
            usuario = Usuario.create(nome=nome, email=email, senha=senha)
            return True, "Usuário cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)
        
    def login(self, email, senha):
        try:
            usuario = Usuario.get(Usuario.email == email)
            if usuario.senha == senha:
                return True, "Login efetuado com sucesso!"
            else:
                return False, "Senha inválida."
        except Usuario.DoesNotExist:
            return False, "Email não encontrado."
        
    def listar(self):
        try:
            usuarios = Usuario.select()
            return [
                print({
                    'id': usuario.id,
                    'nome': usuario.nome,
                    'email': usuario.email
                })
                for usuario in usuarios
            ]
        except Exception as e:
            return str(e)
        
    def atualizar(id, nome, email, senha):
        try:
            usuario = Usuario.get(Usuario.id == id)
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
            usuario.save()
            return True, "Usuário atualizado com sucesso!"
        except Usuario.DoesNotExist:
            return False, "Usuário não encontrado!"
        except Exception as e:
            return False, str(e)

    def excluir(self, id, nome, email, senha):
        try:
            usuario = Usuario.get(Usuario.id == id, Usuario.nome == nome, Usuario.email == email, Usuario.senha == senha)
            usuario.delete_instance()
            return True, "Usuário excluído com sucesso!"
        except Usuario.DoesNotExist:
            return False, "Usuário não encontrado!"
        except Exception as e:
            return False, str(e)
        
    