from credito.arquivo import inicializar_arquivo
from credito.funcoes import interpretar_planilha_credito
from credito.funcoes import gravar_registros_fixos, gravar_registros_variaveis, gravar_registros_gerais, calcular_totais


def gerar_credito():
    inicializar_arquivo()
    registros = interpretar_planilha_credito()

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

    gravar_registros_fixos(fixos)
    gravar_registros_variaveis(variaveis)
    gravar_registros_gerais(gerais)
    calcular_totais(fixos, variaveis, gerais)
