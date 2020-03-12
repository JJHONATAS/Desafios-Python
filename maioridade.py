from datetime import date
total_maior = 0
total_menor = 0
atual = date.today().year

for pessoa in range(1,8):
    nascimento = int(input('Ano de Nascimento {}ª pessoa: '.format(pessoa)))
    idade = atual - nascimento
    if idade < 18:
        total_menor += 1
    else:
        total_maior += 1
print('Ao todo tivemos {} menores de idade'.format(total_menor))
print('e {} maiores de idade.'.format(total_maior))