import csv
from config import caminho_saida_credito
from utils import converter_valor


def inicializar_arquivo():
    with open(caminho_saida_credito, 'w', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Fatura', '', '', '', 'Justificativa'])


def gravar_linha_credito(*args):
    with open(caminho_saida_credito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(args)


def gravar_registros_credito(registros):
    total = 0
    with open(caminho_saida_credito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for registro in registros:
            escritor.writerow(registro.montar_estrutura_csv())
            total += registro.valor
        escritor.writerow(['Total', '', '', converter_valor(total)])
