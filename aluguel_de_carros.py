dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km*0.15)
print('60R$ por dia.')
print('Preço do Km 0.15R$')
print('O total a pagar é de R${}'.format(pago))