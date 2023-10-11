import csv
from utils import converter_valor
from config import esperados_fixos, esperados_variaveis, caminho_entrada_credito
from credito.arquivo import gravar_registros_credito, gravar_linha_credito
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
    gravar_linha_credito('Fixos')
    gravar_registros_credito(registros)


def gravar_registros_variaveis(registros):
    gravar_linha_credito('Variáveis')

    gravar_linha_credito('Gasolina')
    gasolinas = [registro for registro in registros if registro.descricao == 'Gasolina']
    gravar_registros_credito(gasolinas)

    gravar_linha_credito('Santelmo')
    santelmos = [registro for registro in registros if registro.descricao == 'Santelmo']
    gravar_registros_credito(santelmos)


def gravar_registros_gerais(registros):
    gravar_linha_credito('Gerais')
    gravar_registros_credito(registros)


def calcular_totais(registros_fixos, registros_variaveis, registros_gerais):
    gravar_linha_credito('Cálculo')

    gastos_previstos = calcular_soma(registros_fixos) + calcular_soma(registros_variaveis)
    total_fatura = gastos_previstos + calcular_soma(registros_gerais)
    pagamento_antecipado = float(input("Pagamento antecipado: ").replace('.', '').replace(',', '.'))
    outros_gastos = total_fatura - gastos_previstos
    valor_aberto = total_fatura - pagamento_antecipado

    gravar_linha_credito("Gastos Previstos:", '', '', converter_valor(gastos_previstos))
    gravar_linha_credito("Outros Gastos:", '', '', converter_valor(outros_gastos))
    gravar_linha_credito("Pagamento Antecipado:", '', '', converter_valor(pagamento_antecipado))
    gravar_linha_credito("Total Fatura:", '', '', converter_valor(total_fatura))
    gravar_linha_credito("Valor Aberto:", '', '', converter_valor(valor_aberto))
