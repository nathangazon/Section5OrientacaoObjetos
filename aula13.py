'''
@property + @setter = getter e setter no modo python
como getter
p/ evitar quebrar código cliente
p/ habilitar setter
o/ executar ações ao obter um atributo
Atributos que começam com um ou dois underlines _ ou __
não dever ser usados fora da classe.
'''


class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('Estou no getter da cor')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('Estou no setter')
        if valor == 'Rosa':
            raise ValueError('Não é aceita a cor rosa.')
        self._cor = valor

    @property
    def cor_tampa(self):
        print('Estou no getter da tampa')
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('Estou no setter')
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Pink'
# caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
