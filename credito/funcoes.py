import csv
from utils import converter_valor
from config import caminho_entrada_credito
from config import esperados_fixos, esperados_variaveis, caminho_entrada_credito
from arquivo import gravar_registro, gravar_linha
from credito.registro import RegistroCredito


def interpretar_planilha_credito():
    registros = []
    with open(caminho_entrada_credito, 'r', encoding='UTF8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)

        for linha in leitor_csv:
            registro = RegistroCredito(linha)
            registros.append(registro)

    return registros


def calcular_soma(registros):
    soma = 0
    for registro in registros:
        soma += registro.valor
    return soma


def gravar_registros_fixos(registros):
    gravar_linha('credito', 'Fixos')
    gravar_registro('credito',registros)


def gravar_registros_variaveis(registros):
    gravar_linha('credito', 'Variáveis')

    gravar_linha('credito', 'Gasolina')
    gasolinas = [registro for registro in registros if registro.descricao == 'Gasolina']
    gravar_registro('credito',gasolinas)

    gravar_linha('credito', 'Santelmo')
    santelmos = [registro for registro in registros if registro.descricao == 'Santelmo']
    gravar_registro('credito',santelmos)


def gravar_registros_gerais(registros):
    gravar_linha('credito', 'Gerais')
    gravar_registro('credito',registros)


def calcular_totais(registros_fixos, registros_variaveis, registros_gerais):
    gravar_linha('credito', 'Cálculo')

    gastos_previstos = calcular_soma(registros_fixos) + calcular_soma(registros_variaveis)
    total_fatura = gastos_previstos + calcular_soma(registros_gerais)
    pagamento_antecipado = float(input("Pagamento antecipado: ").replace('.', '').replace(',', '.'))
    outros_gastos = total_fatura - gastos_previstos
    valor_aberto = total_fatura - pagamento_antecipado

    gravar_linha('credito', "Gastos Previstos:", '', '', converter_valor(gastos_previstos))
    gravar_linha('credito', "Outros Gastos:", '', '', converter_valor(outros_gastos))
    gravar_linha('credito', "Pagamento Antecipado:", '', '', converter_valor(pagamento_antecipado))
    gravar_linha('credito', "Total Fatura:", '', '', converter_valor(total_fatura))
    gravar_linha('credito', "Valor Aberto:", '', '', converter_valor(valor_aberto))
