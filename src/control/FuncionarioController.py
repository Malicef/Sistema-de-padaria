from src.model.Usuario import *
from src.model.Funcionario import Funcionario

class FuncionarioController:
    @staticmethod
    def cadastrarFuncionario(nome, email, senha, cargo):
        try:
            user = Funcionario.create(nome=nome, email=email, senha=senha, cargo=cargo)
            return True, "Usuário cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)

    @staticmethod
    def loginFuncionario( email, senha):
        try:
            funcionario = Funcionario.get(Funcionario.email == email)
            if funcionario.senha == senha:
                return funcionario
            else:
                return None
        except Funcionario.DoesNotExist:
            return None, "Email não encontrado."

    @staticmethod
    def listarFuncionarios():
        try:
            funcionario = Funcionario.select()
            return [
                print({
                    "nome": funcionario.nome,
                    "email": funcionario.email,
                    "salario": funcionario.salario,
                    "cargo": funcionario.cargo
                })
                for funcionario in funcionario
            ]
        except Exception as e:
            return False, str(e)

    @staticmethod
    def atualizar( id, nome, email, senha, cargo):
        try:
            funcionario = Funcionario.get(Funcionario.id == id)
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha 
            funcionario.cargo = cargo
            funcionario.save()
            return True, "Funcionário atualizado com sucesso!"
        except Exception as e:
            return False, str(e)

    @staticmethod
    def excluirFuncionario(email):
        try:
            Funcionario.delete().where(Funcionario.email == email).execute()
            return True, "Funcionario deletado com sucesso!"
        except Exception as e:
            return False, str(e)