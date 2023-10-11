import registro

esperados_fixos = {
    'Pier',
    'Academia',
    'Amazon Prime',
    'Youtube Premium',
    'curso.dev',
    'Mercado Livre',
    'Psicóloga',
}

esperados_variaveis = {
    'Gasolina',
    'Santelmo'
}
caminhos_entrada = {
    'credito': 'src/credito.csv',
    'debito': 'src/debito.csv'
}

caminhos_saida = {
    'credito': 'output/credito.xlsx',
    'debito': 'output/debito.xlsx'
}

classes = {
    'credito': registro.Credito,
    'debito': registro.Debito
}
