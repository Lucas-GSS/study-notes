print('SOMA DE INTEIROS')

soma = 0
contador = 0
while True:
    numero = int(input('Insira um número inteiro e positivo: '))
    if numero > 0:
        soma += numero
        contador += 1
        continue
    if not numero or numero < 0:
        break

print('Número inválido. Retornando a média dos valores...')
media = soma / contador
print('Média: {}'.format(media.__round__(2)))
