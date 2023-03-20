"""
super() é uma super classe na sub classe. Sobreposição de métodos e atributos

"""


# class MinhaString(str):

#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()  # str=classe, upper()=
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')  # string = instância
# print(string.upper())

class A:
    atributo_a = 'valor a '

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b '

    def __init__(self, atributos, outra_coisa):
        super().__init__(atributos)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c '

    def __init__(self, *args, **kwargs):
        print('Ei, burlei o sistema')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super(C, self).metodo()
        # super(B, self).metodo()
        super().metodo()
        super(B, self).metodo()
        print('C')


c = C('atributo', 'outracoisa')
print(c.atributo)
print(c.outra_coisa)

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
