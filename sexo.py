sexo = 1
while sexo != 'M' and sexo != 'F':
    print('Sexo Inválido!,Tente Novamente!')
    sexo = str(input('Digite seu Sexo[M/F]:')).upper()
print('M para Masculino\nF para feminino')
print('Seu sexo informado foi {}'.format(sexo))
