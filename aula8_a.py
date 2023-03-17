import json
CAMINHO_ARQUIVO = 'aula8.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():

    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('Fazendo o dump.')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


print('isso ', __name__)
if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()
