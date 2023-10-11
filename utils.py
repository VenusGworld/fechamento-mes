def converter_valor(valor: float) -> str:
    valor_convertido = f"{valor:.2f}"
    valor_convertido = valor_convertido.replace('.', ',')
    return valor_convertido


def escolher_campo_extra(*args):
    for campo in args:
        if campo and campo != 'desconhecido':
            return campo
