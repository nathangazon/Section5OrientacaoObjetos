"""
Polimorfismo
"""

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail Enviando:', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS Enviando:', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacão enviada.')
    else:
        print('Notificação Não enviada')


notificacao_email = NotificacaoEmail('testando notificacao')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)
