from utils import converter_valor
from arquivo import inicializar_arquivo, interpretar_planilha, gravar_registros, gravar_linha


def gerar_debito():
    inicializar_arquivo('debito', 'Extrato')
    registros = interpretar_planilha('debito')

    recargas = []
    saidas = []
    entradas = []
    compras = []
    faturas = []
    movimentacoes = []

    total_entradas = 0
    total_saidas = 0

    for registro in registros:
        if registro.valor > 0:
            total_entradas += registro.valor

        if registro.valor < 0:
            total_saidas += registro.valor

        if registro.tipo == 'movimentacao':
            movimentacoes.append(registro)

        elif registro.tipo == 'transferencia recebida':
            entradas.append(registro)

        elif registro.tipo == 'transferencia enviada':
            saidas.append(registro)

        elif registro.tipo == 'recarga':
            recargas.append(registro)

        elif registro.tipo == 'fatura':
            faturas.append(registro)

        elif registro.tipo == 'compra':
            compras.append(registro)

    gravar_linha('debito', 'Movimentações')
    gravar_registros('debito', movimentacoes)

    gravar_linha('debito', 'Entradas')
    gravar_registros('debito', entradas)

    gravar_linha('debito', 'Saidas')
    gravar_registros('debito', saidas)

    gravar_linha('debito', 'Recargas')
    gravar_registros('debito', recargas)

    gravar_linha('debito', 'Faturas')
    gravar_registros('debito', faturas)

    gravar_linha('debito', 'Compras')
    gravar_registros('debito', compras)

    gravar_linha('debito', 'Totais')
    gravar_linha('debito', 'Entradas:', '', '', converter_valor(total_entradas))
    gravar_linha('debito', 'Saídas:', '', '', converter_valor(total_saidas))
    gravar_linha('debito', 'Saldo:', '', '', converter_valor(total_saidas + total_entradas))
