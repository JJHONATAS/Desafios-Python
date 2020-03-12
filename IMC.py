print('\033[1;36m===IMC(Índice de Massa Corporal)===')
peso = float(input('Digite seu Peso em Kg: '))
altura = float(input('Digite sua Altura em metros: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('Peso NORMAL')
elif 25 <= imc <= 30:
    print('Você está SOBREPESO')
elif 30 <= imc <= 40:
    print('Você está na OBESIDADE')
elif imc > 40:
    print('Você está com OBESIDADE GRAVE')
else:
    print('Peso Inválido')