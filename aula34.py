class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome='"Inserir Nome"'):
        print(nome, 'está chamando', self.phone)


call1 = CallMe('229881122121')
call1()
