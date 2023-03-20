"""
Composição é uma especialização da agregação
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append()


class Endereco:
    def __init__(self, rua, numero):
