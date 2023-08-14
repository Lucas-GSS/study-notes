print('Par ou impar')

final = int(input('Insira o valor final da contagem: '))
contador = 1

while contador <= final:
    if (contador % 2 == 0):
        print('{} é par'.format(contador))
    else:
        print('{} é ímpar'.format(contador))
    contador += 1
