from datetime import date
print('\033[4;36m CONFEDERAÇÃO NACIONAL DE NATAÇÃO \033[m')
nascimento = int(input('  \033[1m Em Qual ano você nasceu? '))
atual = date.today().year
idade = atual - nascimento
print('Quem Nasceu em {} tem {} anos em {}.'.format(nascimento,idade,atual))
if idade <= 9:
    print('Você está na categoria  \033[1;36;40m MIRIM.  \033[m ')
elif 9 <=  idade <= 14:
    print('Você está na categoria  \033[1;33;40m INFANTIL.  \033[m ')
elif 14 <=  idade <= 19:
    print('Você está na categoria  \033[1;32;40m JUNIOR.  \033[m ')
elif idade == 20:
    print('Você está na categoria  \033[1;31;40m SÊNIOR.  \033[m ')
elif idade > 20:
    print('Você está na categoria  \033[1;35;40m MASTER.  \033[m ')
else:
    print('CATEGORIA INVÁLIDA')