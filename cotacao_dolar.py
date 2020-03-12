real = float(input('Quanto dinheiro você tem na real? R$ '))
print(real,'Na real!')
dolar = real / 3.97
print('Com R$ {:.2f} você consegue comprar U$$ {:.2f}'.format(real,dolar))
print('dólar U$$1.00 = R$3.97')
