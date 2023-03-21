# classes decoradoras (decorator classes)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            retorno = func(*args, **kwargs)
            return retorno * self._multiplicador
        return interna


@Multiplicar(10)
def soma(x, y):
    return x + y


dois_mais_dois = soma(2, 4)
print(dois_mais_dois)
