print('----------------', '\n', 'CONTADOR', '\n', '-----------------')
start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))


def contador(inicio, fim, passo):
    for i in range(inicio, fim + 1, passo):
        print('{}'.format(i), end='')


contador(start, end, step)
