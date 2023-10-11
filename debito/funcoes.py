import csv
from config import caminho_entrada_debito
from debito.registro import RegistroDebito


def interpretar_planilha_debito():
    with open(caminho_entrada_debito, 'r', encoding='UTF8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)
        registros = [RegistroDebito(linha) for linha in leitor_csv]
    return registros
