from datetime import date
print('\033[1;32m ===ALISTAMENTO MILITAR=== ')
nascimento= int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} tem {} em {}'.format(nascimento,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade 
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
 