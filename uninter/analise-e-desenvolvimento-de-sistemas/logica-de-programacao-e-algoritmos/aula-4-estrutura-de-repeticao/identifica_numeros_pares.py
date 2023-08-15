print('Identificador de núemros pares')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
x = inicio
while x <= fim:
    if (x % 2 == 0):
        print(x)
    x += 1

print('Fim')
