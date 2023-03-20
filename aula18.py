

class Car:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabric = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabric(self):
        return self._fabric

    @fabric.setter
    def fabric(self, valor):
        self._fabric = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabric:
    def __init__(self, nome):
        self.nome = nome


fusca = Car('Fusca')
volkswagen = Fabric('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabric = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabric.nome, fusca.motor.nome)

fiat_uno = Car('Uno')
fiat = Fabric('Fiat')
motor_1_0 = Motor('1.0')
fiat_uno.fabric = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabric.nome, fiat_uno.motor.nome)
