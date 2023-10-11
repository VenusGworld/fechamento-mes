import csv
from datetime import datetime
from utils import converter_valor
from config import caminho_saida_debito


def inicializar_arquivo():
    with open(caminho_saida_debito, 'w', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Débito', '', '', '', 'Justificativa'])


def gravar_linha_debito(*args):
    with open(caminho_saida_debito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(args)


def gravar_registros_debito(registros):
    total = 0
    with open(caminho_saida_debito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for registro in registros:
            escritor.writerow(registro.montar_estrutura_csv())
            total += registro.valor
        escritor.writerow(['Total', '', '', converter_valor(total)])
