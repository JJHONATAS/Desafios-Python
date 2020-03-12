from time import sleep
print(10*' \033[1;31m *','CONTAGEM REGRESSIVA',10*' \033[1;31m *')
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(10*'*','BOMMMMM',10*'*')