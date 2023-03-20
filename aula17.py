"""
Composição é uma especialização da agregação
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def __del__(self):
        print('APAGANDO', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO, ', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 44)
cliente1.inserir_endereco('Rua B', 3331)
cliente1.listar_enderecos()
endereco_externo = Endereco('Av Saudade', 11122)
cliente1.inserir_endereco_externo(endereco_externo)

del cliente1

print(endereco_externo.rua, endereco_externo.numero)
print('################Aqui termina o meu codigo')
