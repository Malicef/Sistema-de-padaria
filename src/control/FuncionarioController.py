from src.model.Usuario import *
from src.model.Funcionario import Funcionario

class FuncionarioController:
    def cadastrar(nome, email, senha, salario, cargo):
        try:
            user = Funcionario.create(nome=nome, email=email, senha=senha, salario=salario, cargo=cargo)
            return True, "Usuário cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)
        
    def login( email, senha):
        try:
            funcionario = Funcionario.get(Funcionario.email == email)
            if funcionario.senha == senha:
                return funcionario
            else:
                return False, "Senha inválida!"
        except Funcionario.DoesNotExist:
            return False, "Email não cadastrado!"
    
    def listar():
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
        
    def atualizar( id, nome, email, senha, salario, cargo):
        try:
            funcionario = Funcionario.get(Funcionario.id == id)
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha 
            funcionario.salario = salario
            funcionario.cargo = cargo
            funcionario.save()
            return True, "Funcionário atualizado com sucesso!"
        except Exception as e:
            return False, str(e)
    
    def deletar(email):
        try:
            Funcionario.delete().where(Funcionario.email == email).execute()
            return True, "Funcionario deletado com sucesso!"
        except Exception as e:
            return False, str(e)
        