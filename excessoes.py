def square(n):
    try:
        return n ** 2
    except:
        print('Parâmetro Inválido.Uma Excessão ocorreu.')
    finally:
        print('Eu Sempre serei executado.')
print(square(9))
square(9)
print(square(2))
print(square('4'))
