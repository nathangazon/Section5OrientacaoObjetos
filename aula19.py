"""
herança -classe principal e classe filhas
"""


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Nathan', 'Gazon')
c1.falar_nome_classe()
c2 = Aluno('Reinaldo', 'Azevedo')
c2.falar_nome_classe()
