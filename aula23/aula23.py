# Abstração
from pathlib import Path
from abc import ABC, abstractmethod

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Oi')
