import csv
from config import esperados_fixos, esperados_variaveis, caminho_entrada_credito
from credito.arquivo import gravar_registros_credito, gravar_linha_credito
from credito.registro import RegistroCredito


def interpretar_planilha_credito():
    registros_fixos = []
    registros_variaveis = []
    registros_gerais = []

    with open(caminho_entrada_credito, 'r', encoding='UTF8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        next(leitor_csv)

        for linha in leitor_csv:
            registro = RegistroCredito(linha)

            if registro.categoria != 'payment':
                if registro.descricao in esperados_fixos:
                    registros_fixos.append(registro)

                elif registro.descricao in esperados_variaveis:
                    registros_variaveis.append(registro)

                else:
                    registros_gerais.append(registro)

    return registros_fixos, registros_variaveis, registros_gerais


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

    registro_unico_gasolina = RegistroCredito()
    registro_unico_gasolina.valor = 0

    registro_unico_santelmo = RegistroCredito()
    registro_unico_santelmo.valor = 0

    for registro in registros:
        if registro.descricao == 'Gasolina':
            registro_unico_gasolina.data = registro.data
            registro_unico_gasolina.categoria = registro.categoria
            registro_unico_gasolina.descricao = registro.descricao
            registro_unico_gasolina.valor += registro.valor

        if registro.descricao == 'Santelmo':
            registro_unico_santelmo.data = registro.data
            registro_unico_santelmo.categoria = registro.categoria
            registro_unico_santelmo.descricao = registro.descricao
            registro_unico_santelmo.valor += registro.valor

    gravar_registros_credito([registro_unico_gasolina, registro_unico_santelmo])


def calcular_totais(registros_fixos, registros_variaveis, registros_gerais):
    gravar_linha_credito('Cálculo')

    gastos_previstos = calcular_soma(registros_fixos) + calcular_soma(registros_variaveis)
    total_fatura = gastos_previstos + calcular_soma(registros_gerais)
    pagamento_antecipado = float(input("Pagamento antecipado: ").replace('.', '').replace(',', '.'))
    outros_gastos = total_fatura - gastos_previstos
    valor_aberto = total_fatura - pagamento_antecipado

    gravar_linha_credito(f"Gastos Previstos: {gastos_previstos:.2f}")
    gravar_linha_credito(f"Outros Gastos: {outros_gastos:.2f}")
    gravar_linha_credito(f"Pagamento Antecipado: {pagamento_antecipado:.2f}")
    gravar_linha_credito(f"Total Fatura: {total_fatura:.2f}")
    gravar_linha_credito(f"Valor Aberto: {valor_aberto:.2f}")
