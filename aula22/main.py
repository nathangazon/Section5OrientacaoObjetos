# from log import LogPrintMixin, LogFileMixin

# lp = LogPrintMixin()
# lp.log_error('Qualquer coisa')
# lp.log_success('Funcionou')


# lf = LogFileMixin()
# lf.log_error('Qualquer coisa')
# lf.log_success('Funcionou')


from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()
