print('====Triangulo====')
a= int(input('Primeira Reta: '))
b = int(input('Segunda Reta: '))
c = int(input('Terceira Reta: '))
if  b - c < a < b + c and a - c < b < a + c and a - b  < c < a + b:
    print('Forma Um Triângulo')
else:
    print('Não Forma um Triângulo')