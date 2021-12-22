#SISTEMA CONTA CORRENTE
from datetime import datetime, timezone

class ContaCorrente():
    """
    Cria um objeto conta corrente para gerencia as contas correntes.

    Attributos:
        nome: (str) Nome do Cliente
        cpf: (str) Cpf do Cliente com pontos e traço
        Agencia: (int) Agencia responsável pela conta do cliente.
        num_conta: (int) Número da conta corrente do cliente
        saldo: (float) Saldo atual da conta do cliente
        limite: (float) Limite de cheque especial
        tansacoes: (list) Extrato de transações da conta do cliente

    """
    @staticmethod
    def _data_hora():
        """
        Pega data e hora atual no formato adequado.
        """
        hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return hora

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self._nome = nome
        self._cpf = cpf
        self._limite = None
        self._saldo = 0
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        return f"_saldo: R$ {self._saldo}"

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito
        self._transacoes.append((valor_deposito, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite =  -1000
        return self._limite

    def sacar(self, valor_sacado):
        if  self._saldo - valor_sacado < self._limite_conta():
            print('Você não tem aldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor_sacado
            self._transacoes.append((valor_sacado, self._saldo, ContaCorrente._data_hora()))

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))       
    
    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque especial é de R$ {self._limite_conta():.2f}')        

    def extrato_bancario(self):
        print('EXTRATO BANCÁRIO')
        for transacao in self._transacoes:
            print(transacao)


class CartaoCredito:

    def __init__(self, titular, conta_corrente) -> None:
        self.numero = 1234
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)