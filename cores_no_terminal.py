print('\033[31;7;43m Olá, Mundo! \033[m')
a = input('Digite para valor de a: ')
b = input('Digitie para valor de b: ')
print('Os valores são \033[32m {} \033[m e \033[31m {}\033[m'.format(a,b))
nome = input('Qual o seu nome? ')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoEbranco':'\033[7;30m'   
}
print('Olá! Muito prazer em te conhecer {} {} {}!!!'.format(cores['amarelo'],nome,cores['limpa']))
print('Olá! Muito prazer em te conhecer {} {} {}!!!'.format('\033[4;34m',nome,'\033[m'))
#pintando # \033[style 0 a 7;text 30 a 37;back 40 a 47m \033[m
