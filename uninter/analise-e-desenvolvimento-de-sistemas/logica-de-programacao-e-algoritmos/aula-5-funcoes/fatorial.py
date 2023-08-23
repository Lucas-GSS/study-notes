def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


entrada = int(input("Insira um número: "))

while entrada < 0:
    entrada = int(input("Insira um número: "))

print("O fatorial de {} é: {}".format(entrada, fatorial(entrada)))
