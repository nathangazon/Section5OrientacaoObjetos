# atributos de classe
ANO_ATUAL = 2023


class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 30)
p2 = Pessoa('Helena', 12)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
