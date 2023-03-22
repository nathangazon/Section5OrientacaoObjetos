"""
daclasses - o que são dataclasses?
o módulo dataclasses ofereces decorators e funções para criar métodos como
__init__(), __repr__(), __eq__(), entre outros, em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar para cirar classes normais.
Fio descrito na PEP 557 e adicionado na versão 3.7 do Python.
doc:
"""

from dataclasses import dataclass, field


# @dataclass(init=False)
@dataclass
class Pessoa:
    nome: str = field(default='Missing')
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)
