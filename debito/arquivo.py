import csv
from datetime import datetime
from config import caminho_saida_debito


def inicializar_arquivo():
    with open(caminho_saida_debito, 'w', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Relatorio Debito'])


def gravar_linha_debito(conteudo):
    with open(caminho_saida_debito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([str(conteudo)])


def gravar_registros_debito(registros):
    hoje = datetime.now().strftime('%d/%m/%Y')
    total = 0
    with open(caminho_saida_debito, 'a', encoding='UTF8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for registro in registros:
            escritor.writerow(registro.montar_estrutura_csv())
            total += registro.valor
        escritor.writerow([hoje, 'total', total])
