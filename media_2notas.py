print(' \033[1m MÉDIA DO ALUNO ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) /2
if media < 5:
    print('Sua média  \033[1;31m {:.2f} \033[m está \033[1;31m REPROVADA. \033[m '.format(media))
elif  5 <= media <= 6.9:
    print('Sua média é \033[1;34m {:.2f} \033[m portanto está de \033[1;34m RECUPERAÇÃO. \033[m '.format(media))
else:
    print('Sua média \033[1;32m {:.2f} \033[m está \033[1;32m APROVADA! \033[m '.format(media))    