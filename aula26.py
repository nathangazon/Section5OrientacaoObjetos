class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('A mensgem do meu erro')
    raise exception_


try:
    1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('VOu lançar de novo')
    raise exception_ from error
