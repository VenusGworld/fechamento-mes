from utils import somar_registros, solicitar_valor_input
from planilha import inicializar_arquivo, interpretar_planilha, gravar_registros, gravar_linha, formatar_planilha


def gravar_fixos(registros):
    gravar_linha('credito', 'Fixos')
    gravar_registros('credito', registros)


def gravar_variaveis(registros):
    gravar_linha('credito', 'Variáveis')

    gasolinas = []
    santelmos = []

    for registro in registros:
        if registro.descricao == 'Gasolina':
            gasolinas.append(registro)

        if registro.descricao == 'Santelmo':
            santelmos.append(registro)

    gravar_registros('credito', gasolinas)
    gravar_registros('credito', santelmos)


def gravar_gerais(registros):
    gravar_linha('credito', 'Gerais')
    gravar_registros('credito', registros)


def gravar_calculo(fixos, variaveis, gerais):
    gravar_linha('credito', 'Cálculo')

    gastos_previstos = somar_registros(fixos) + somar_registros(variaveis)
    total_fatura = gastos_previstos + somar_registros(gerais)
    pagamento_antecipado = solicitar_valor_input("Pagamento antecipado: ")
    outros_gastos = total_fatura - gastos_previstos
    valor_aberto = total_fatura - pagamento_antecipado

    gravar_linha('credito', "Gastos Previstos", gastos_previstos)
    gravar_linha('credito', "Outros Gastos", outros_gastos)
    gravar_linha('credito', "Pagamento Antecipado", pagamento_antecipado)
    gravar_linha('credito', "Total Fatura", total_fatura)
    gravar_linha('credito', "Valor Aberto", valor_aberto)


def gerar_credito():
    inicializar_arquivo('credito', 'Fatura')
    registros = interpretar_planilha('credito')

    fixos = []
    variaveis = []
    gerais = []

    for registro in registros:
        if registro.tipo == 'fixo':
            fixos.append(registro)

        if registro.tipo == 'variavel':
            variaveis.append(registro)

        if registro.tipo == 'geral':
            gerais.append(registro)

    gravar_fixos(fixos)
    gravar_variaveis(variaveis)
    gravar_gerais(gerais)
    gravar_calculo(fixos, variaveis, gerais)
    formatar_planilha('credito')
