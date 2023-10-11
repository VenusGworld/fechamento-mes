class RegistroDebito:
    def __init__(self, linha=None):
        if linha:
            self.data = linha[0]
            self.valor = float(linha[1])
            self.identificador = linha[2]
            self.descricao = linha[3]
            self.envolvido = 'desconhecido'
            self.tipo = 'desconhecido'

        if 'Transferência' in self.descricao and self.valor > 0:
            self.tipo = 'transferencia recebida'
            self.envolvido = self.descricao.split(' - ')[1].title()

        if 'Transferência' in self.descricao and self.valor < 0:
            self.tipo = 'transferencia enviada'
            self.envolvido = self.descricao.split(' - ')[1].title()

        if 'Recarga' in self.descricao:
            self.tipo = 'recarga'

        if 'fatura' in self.descricao:
            self.tipo = 'fatura'

        if 'Compra' in self.descricao:
            self.tipo = 'compra'
            self.envolvido = self.descricao.split(' - ')[1].title()

        if 'anthony' in self.envolvido.lower():
            self.tipo = 'movimentacao'

    def montar_estrutura_csv(self):
        return [self.data, self.tipo, self.envolvido, self.valor]

    def __str__(self):
        return f"{self.data} | {self.tipo} | {self.valor}"
