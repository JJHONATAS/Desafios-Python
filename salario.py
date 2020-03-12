salario = float(input('Qual o seu salário? R$ '))
if salario <= 1250:
    novo_salario = (salario *15/100) + salario
    print('Aumento de 10%,Seu novo salário é de {:.2f} R$'.format(novo_salario))
else:
    novo_salario = (salario*10/100)+ salario
    print('Aumento de 15%,Seu novo salário é de {:.2f} R$'.format(novo_salario))