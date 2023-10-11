import csv
from utils import converter_valor
from config import caminho_entrada_credito, caminho_entrada_debito, caminho_saida_credito, caminho_saida_debito
from registro import Credito, Debito


def interpretar_planilha(tipo):
    if tipo == 'credito':
        caminho = caminho_entrada_credito
        classe = Credito

    if tipo == 'debito':
        caminho = caminho_entrada_debito
        classe = Debito

    with open(caminho, 'r', encoding='UTF8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)
        registros = [classe(linha) for linha in leitor_csv]

    return registros


def inicializar_arquivo(tipo, titulo):
    if tipo == 'credito':
        caminho = caminho_saida_credito

    if tipo == 'debito':
        caminho = caminho_saida_debito

    with open(caminho, 'w', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([titulo, '', '', '', 'Justificativa'])


def gravar_linha(tipo, *args):
    if tipo == 'credito':
        caminho = caminho_saida_credito

    if tipo == 'debito':
        caminho = caminho_saida_debito

    with open(caminho, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(args)


def gravar_registros(tipo, registros):
    if tipo == 'credito':
        caminho = caminho_saida_credito

    if tipo == 'debito':
        caminho = caminho_saida_debito

    total = 0
    with open(caminho, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for registro in registros:
            escritor.writerow(registro.montar_estrutura_csv())
            total += registro.valor
        escritor.writerow(['Total', '', '', converter_valor(total)])
