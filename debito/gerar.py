from utils import converter_valor
from arquivo import inicializar_arquivo, gravar_linha, gravar_registro
from debito.funcoes import interpretar_planilha_debito


def gerar_debito():
    inicializar_arquivo('debito', 'Extrato')
    registros = interpretar_planilha_debito()

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
    gravar_registro('credito', movimentacoes)

    gravar_linha('debito', 'Entradas')
    gravar_registro('credito', entradas)

    gravar_linha('debito', 'Saidas')
    gravar_registro('credito', saidas)

    gravar_linha('debito', 'Recargas')
    gravar_registro('credito', recargas)

    gravar_linha('debito', 'Faturas')
    gravar_registro('credito', faturas)

    gravar_linha('debito', 'Compras')
    gravar_registro('credito', compras)

    gravar_linha('debito', 'Totais')
    gravar_linha('debito', 'Entradas:', '', '', converter_valor(total_entradas))
    gravar_linha('debito', 'Saídas:', '', '', converter_valor(total_saidas))
    gravar_linha('debito', 'Saldo:', '', '', converter_valor(total_saidas + total_entradas))
