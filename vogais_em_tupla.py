palavra = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR',
           'TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

for vogais in palavra:
    print(f'\nNa palavra {vogais.upper()} temos ', end= ' ')
    for letra in vogais:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')