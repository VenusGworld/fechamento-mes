class RegistroCredito:
    def __init__(self, linha=None):
        if linha:
            self.data = linha[0]
            self.categoria = linha[1]
            self.descricao = linha[2]
            self.valor = float(linha[3])

    def montar_estrutura_csv(self):
        return [self.data, self.descricao, self.valor]

    def __str__(self):
        return f"{self.data} | {self.categoria} | {self.descricao} | {self.valor}"
