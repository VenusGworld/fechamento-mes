import csv
from config import caminho_saida_credito


def inicializar_arquivo():
    with open(caminho_saida_credito, 'w', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Fatura'])


def gravar_linha_credito(conteudo):
    with open(caminho_saida_credito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([str(conteudo)])


def gravar_registros_credito(registros):
    with open(caminho_saida_credito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for registro in registros:
            escritor.writerow(registro.montar_estrutura_csv())
