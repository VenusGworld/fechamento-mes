def somar_registros(registros: list) -> float:
    soma = 0
    for registro in registros:
        soma += registro.valor
    return soma


def solicitar_valor_input(mensagem: str) -> float:
    resposta = input(mensagem)
    resposta = resposta.replace('.', '').replace(',', '.')
    valor = float(resposta)
    return valor


def converter_valor(valor: float) -> str:
    valor_convertido = f"{valor:.2f}"
    valor_convertido = valor_convertido.replace('.', ',')
    return valor_convertido


def escolher_campo_extra(*args):
    for campo in args:
        if campo and campo != 'desconhecido':
            return campo
