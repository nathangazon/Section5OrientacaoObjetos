# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 30}
p1 = Pessoa(**dados)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Eitcha'
# del p1.__dict__['nome']
# # p1.nome = 'Eita'
# print(p1.idade)
# print(p1.__dict__)
print(vars(p1))
print(*dados)
