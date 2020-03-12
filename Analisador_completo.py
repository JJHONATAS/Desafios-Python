soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ' '
total_mulher20 = 0
for pessoa in range(1,5):
    print('------{}ª PESSOA-------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:   '))
    sexo = str(input('Sexo [M/F]:   ')).strip().upper()
    soma_idade += idade

    if pessoa == 1 and sexo in 'Mm': #SE FOR A 1 PESSOA
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher20 += 1
media_idade = soma_idade /  4
print('A média das idades das pessoas do grupo é {}'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem,nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher20))