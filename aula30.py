

# with open('aula30.txt', 'w') as arquivo:
#     ...

class MyOpen:

    def __init__(self, caminho_arquivo, modo):
        print('INIT')
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()

        raise class_exception(*exception_.args)

        print(class_exception)
        print(exception_)
        print(traceback_)

        return True


instancia = MyOpen('aula30.txt', 'w')
with instancia as arquivo:
    arquivo.write('Line 1\n')
    arquivo.write('Line 2\n', 123)
    arquivo.write('Line 3\n')
    print('WITH', arquivo)
