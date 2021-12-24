#SISTEMA CONTA CORRENTE
from datetime import datetime, timezone
import pytz
from random import randint

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
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return data_hora

    def __init__(self, nome, cpf, agencia, num_conta) -> None:
        self.nome = nome
        self.cpf = cpf
        self._limite = None
        self._saldo = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

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

    @staticmethod
    def _data_hora():
        """
        Pega data e hora atual no formato adequado.
        """
        data_hora = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return data_hora

    def __init__(self, titular, conta_corrente) -> None:
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora()[3:5], int(CartaoCredito._data_hora()[6:10]) + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
    
    
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print("Senha alterada com sucesso.")
        else:
            print("Nova senha inválida.")