#Python

conta = int(input('Informe o numero da sua conta:'))
saldo = float(input('Informe o seu saldo: '))
debito = float(input('Informe o valor do débito: '))
credito = float(input('Informe o valor do crédito: '))

saldoatual = saldo - debito + credito
print('Seu saldo atual é de {0:.2f} reais.'.format(saldoatual))
if saldoatual >= 0:
    print('Saldo Positivo')
else:
    print('Salvo Negativo')