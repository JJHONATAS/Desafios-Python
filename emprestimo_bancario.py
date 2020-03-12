print('\033[1;33;40m EMEPRÉSTIMO BANCÁRIO')
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = float(input('Em quantos anos vai pagar? '))
prestacao_mensal = casa / (anos * 12)
minimo = salario * (30/100)
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,anos))
print('a prestação será de R$ {:.2f}'.format(prestacao_mensal))
if  prestacao_mensal <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')