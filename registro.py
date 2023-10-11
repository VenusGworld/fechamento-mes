from utils import converter_valor, escolher_campo_extra
from config import esperados_fixos, esperados_variaveis


class Credito:
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


class Debito:
    def __init__(self, linha=None):
        if linha:
            self.data = linha[0]
            self.valor = float(linha[1])
            self.identificador = linha[2]
            self.descricao = linha[3]
            self.envolvido = 'desconhecido'
            self.tipo = 'desconhecido'
            self.banco = 'desconhecido'

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
            self.envolvido = None
            descricao_bancaria = self.descricao.split(' - ')[3].lower()

            if 'santander' in descricao_bancaria:
                self.banco = 'santander'

            if 'xp' in descricao_bancaria:
                self.banco = 'rico'

    def montar_estrutura_csv(self):
        campo_extra = escolher_campo_extra(self.envolvido, self.banco, self.identificador)
        return [self.data, self.tipo, campo_extra, converter_valor(self.valor)]

    def __str__(self):
        campo_extra = escolher_campo_extra(self.envolvido, self.banco, self.identificador)
        return f"{self.data} | {self.tipo} | {campo_extra} | {converter_valor(self.valor)}"
