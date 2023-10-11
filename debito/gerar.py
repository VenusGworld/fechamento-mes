from utils import converter_valor
from debito.arquivo import inicializar_arquivo, gravar_linha_debito, gravar_registros_debito
from debito.funcoes import interpretar_planilha_debito


def gerar_debito():
    inicializar_arquivo()
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

        else:
            print(f"Erro no registro: {registro}")

    gravar_linha_debito('Movimentações')
    gravar_registros_debito(movimentacoes)

    gravar_linha_debito('Entradas')
    gravar_registros_debito(entradas)

    gravar_linha_debito('Saidas')
    gravar_registros_debito(saidas)

    gravar_linha_debito('Recargas')
    gravar_registros_debito(recargas)

    gravar_linha_debito('Faturas')
    gravar_registros_debito(faturas)

    gravar_linha_debito('Compras')
    gravar_registros_debito(compras)

    gravar_linha_debito('Totais')
    gravar_linha_debito('Entradas:', '', '', converter_valor(total_entradas))
    gravar_linha_debito('Saídas:', '', '', converter_valor(total_saidas))
    gravar_linha_debito('Saldo:', '', '', converter_valor(total_saidas + total_entradas))
