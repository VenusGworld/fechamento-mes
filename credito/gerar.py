from credito.arquivo import inicializar_arquivo
from credito.funcoes import interpretar_planilha_credito
from credito.funcoes import gravar_registros_fixos, gravar_registros_variaveis, calcular_totais


def gerar_credito():
    inicializar_arquivo()
    registros_fixos, registros_variaveis, registros_gerais = interpretar_planilha_credito()
    gravar_registros_fixos(registros_fixos)
    gravar_registros_variaveis(registros_variaveis)
    calcular_totais(registros_fixos, registros_variaveis, registros_gerais)
