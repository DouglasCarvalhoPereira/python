from contabanco import ContaCorrente

cliente_1 = ContaCorrente('Douglas', '23.345.567-99', 1020, 2344)
cliente_2 = ContaCorrente('Clayton', '26.305.561-30', 1021, 2342)

print(cliente_1.consultar_saldo())
cliente_1.depositar(100)
cliente_1.depositar(2000)
cliente_1.sacar(100)
cliente_1.depositar(10000000)
cliente_1.extrato_bancario()
cliente_1.transferir(1000, cliente_2)
print(cliente_2.consultar_saldo())
cliente_2.extrato_bancario()