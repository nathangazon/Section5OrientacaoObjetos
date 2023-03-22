import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Depósito ${valor:.2f})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é ${self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE ${valor:.2f})')
            return self.saldo

        print('Não foi possível realizar o valor desejado')
        self.detalhes(f'(Saque Negado ${valor:.2f})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE ${valor:.2f}).')
            return self.saldo

        print('Não foi possível realizar o valor desejado.')
        print('Seu limite é -${self.limite:.2f}.')
        self.detalhes(f'(Saque Negado ${valor:.2f}).')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
            f'{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.detalhes()
    cp1.sacar(.23)
    cp1.sacar(1.11)
    cp1.sacar(1.32)
    cp1.sacar(1.32)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.detalhes()
    cc1.sacar(.23)
    cc1.sacar(1.11)
    cc1.sacar(1.32)
    cc1.sacar(97)
    cc1.sacar(97)
    print('##')
