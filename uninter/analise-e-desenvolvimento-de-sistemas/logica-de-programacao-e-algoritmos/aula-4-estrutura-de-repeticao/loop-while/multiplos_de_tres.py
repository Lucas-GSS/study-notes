print('Multiplos de 3')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
x = inicio
contador = 0
while x <= fim and contador <= 10:
    if x % 3 == 0:
        print(x)
        contador += 1
    x += 1
