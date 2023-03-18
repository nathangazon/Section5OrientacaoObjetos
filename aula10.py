class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('OI', args, kwargs)

    def funcao(*args, **kwargs):
        print('OI', args, kwargs)


c1 = Classe()
c1.funcao_que_esta_na_classe(12, 2, 5)
Classe.funcao(12, 2, 5)
Classe.funcao_que_esta_na_classe(nome=1)
