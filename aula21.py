"""
herança múltipla - python orientados a objetos
mro() - method resolution order
__mro__ - dunder double 
"""


class A():
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
print(D.__mro__)
D.mro()
