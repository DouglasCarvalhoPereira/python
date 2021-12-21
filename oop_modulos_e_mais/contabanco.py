#SISTEMA CONTA CORRENTE
from datetime import datetime, timezone

class ContaCorrente():
    
    @staticmethod
    def _data_hora():
        hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return hora

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self.nome = nome
        self.cpf = cpf
        self.limite = None
        self.saldo = 0
        self.agencia = agencia
        self.conta = num_conta
        self.transacoes = []


    def consultar_saldo(self):
        return f"Saldo: R$ {self.saldo}"

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.transacoes.append((valor_deposito, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite =  -1000
        return self.limite

    def sacar(self, valor_sacado):
        if  self.saldo - valor_sacado < self._limite_conta():
            print('Você não tem aldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor_sacado
            self.transacoes.append((valor_sacado, self.saldo, ContaCorrente._data_hora()))

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))       
    
    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque especial é de R$ {self._limite_conta():.2f}')        

    def extrato_bancario(self):
        print('EXTRATO BANCÁRIO')
        for transacao in self.transacoes:
            print(transacao)