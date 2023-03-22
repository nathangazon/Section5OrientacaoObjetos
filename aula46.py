from collections.abc import Iterable


class MyList(Iterable):
    def __init__(self):
        self._data = {}
        self._index = 0

    def append(self, value):
        self._data[self._index] = value
        self._index += 1

    def __iter__(self):
        ...


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria')
    lista.append('Maria')
    print(lista._data)
