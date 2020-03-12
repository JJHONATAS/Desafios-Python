preço = float(input('Qual o Preço do seu produto? R$'))
desconto = preço - (preço*5/100)
print('Seu produto{:.2f} com desconto de 5%  será {:.2f} R$ '.format(preço,desconto))