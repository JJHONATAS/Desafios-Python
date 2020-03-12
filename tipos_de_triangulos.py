print(' \033[7;40m TIPOS DE TRIÂNGULOS \033[m')
a = float(input('Digite o valor do Segmento\033[1m A:\033[m'))
b = float(input('Digite o valor do Segmento\033[1m B:\033[m'))
c = float(input('Digite o valor do Segmento\033[1m C:\033[m'))
if a < b+ c and b < a + c and c < a + b:
    if a == b and b == c:
        print(' \033[1;32m Triângulo Equilátero')
    else:
        if a == b or a == c or c == b:
            print(' \033[1;34m Triângulo Isósceles')
        else:
            print(' \033[1;33m Triângulo Escaleno')
else:
    print('Não é Triângulo')