from classes.contaPoupanca import ContaPoupanca
from classes.contaCorrente import ContaCorrente

conta1 = ContaPoupanca(agencia=123, conta='P01', saldo=0)
conta1.depositar(20)
conta1.sacar(15)
conta1.sacar(5)
conta1.sacar(1)
print()
print('=' * 80)
print()
conta2 = ContaCorrente(agencia=321, conta='C01', saldo=0)
conta2.depositar(10)
conta2.sacar(90)
conta2.sacar(30)
conta2.depositar(200)

