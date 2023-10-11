from utils import converter_valor
from config import esperados_fixos, esperados_variaveis


class RegistroCredito:
    def __init__(self, linha=None):
        if linha:
            self.data = linha[0]
            self.categoria = linha[1]
            self.descricao = linha[2]
            self.valor = float(linha[3])

        if self.categoria in 'payment':
            self.tipo = 'pagamento antecipado'

        elif self.descricao in esperados_fixos:
            self.tipo = 'fixo'

        elif self.descricao in esperados_variaveis:
            self.tipo = 'variavel'

        else:
            self.tipo = 'geral'

    def montar_estrutura_csv(self):
        return [self.data, self.tipo, self.descricao, converter_valor(self.valor)]

    def __str__(self):
        return f"{self.data} | {self.tipo} | {self.categoria} | {self.descricao} | {converter_valor(self.valor)}"
