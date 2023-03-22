# metaclasses são os tipos das classes.
def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__}))'


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1345
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente método falar')

        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        print(instancia.__dict__)
        return instancia


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu NEW')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        print('falando.....')


p1 = Pessoa('Luiz')
print(p1.attr)
print(p1)
