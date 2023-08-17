for numero in range(2, 100):
    red_flag = 0
    for i in range(2, numero, 100):
        if (numero % i == 0):
            red_flag = 1
            break
    if (not red_flag):
        print(numero)
