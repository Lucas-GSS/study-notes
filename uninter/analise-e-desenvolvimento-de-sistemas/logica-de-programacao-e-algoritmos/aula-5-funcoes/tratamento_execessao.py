def divisao():
    try:
        dividendo = int(input('Insira o dividendo: '))
        divisor = int(input('Insira o divisor: '))
        resultado = dividendo / divisor
        print(resultado)
    except ZeroDivisionError:
        print('Ops... Não é possível dividir por zero')
        return True
    except ValueError:
        print('Insira um NÚMERO')
        return True


while divisao():
    divisao()
