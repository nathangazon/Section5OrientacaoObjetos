"""
daclasses - o que são dataclasses?
o módulo dataclasses ofereces decorators e funções para criar métodos como 
__init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar para cirar classes normais.
Fio descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc: 
"""

from dataclasses import dataclass


# @dataclass(init=False)
@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('POST INIT')
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':

    p1 = Pessoa('Nathan', 'Gazon')
    print(p1)
