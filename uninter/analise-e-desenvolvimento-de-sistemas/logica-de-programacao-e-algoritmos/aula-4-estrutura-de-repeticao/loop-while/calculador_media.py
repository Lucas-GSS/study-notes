print('Calculador Media')
contador = 1
acumulador = 0

while contador <= 5:
    valor = int(input('Insira a {}ª nota: '.format(contador)))
    acumulador += valor
    contador += 1

media = acumulador / 5

print('Média: {}'.format(media.__round__(2)))
