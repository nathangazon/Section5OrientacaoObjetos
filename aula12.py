class Caneta():
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Property')
        return self.cor_tinta

    @property  # se comporta como atributo em python, ou seja, não deve ser chamado como método
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


# class Caneta():
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('Get cor')
#         return self.cor_tinta


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
