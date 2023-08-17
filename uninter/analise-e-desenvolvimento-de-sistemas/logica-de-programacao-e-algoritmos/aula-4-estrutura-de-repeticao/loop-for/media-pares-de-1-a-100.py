soma = 0
contador_pares = 0

for i in range(1, 101):
    if (i % 2 == 0):
        soma += i
        contador_pares += 1

media = soma / contador_pares

print('Média: {}'.format(media))
