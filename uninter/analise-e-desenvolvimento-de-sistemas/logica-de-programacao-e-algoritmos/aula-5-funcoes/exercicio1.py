nome_usuario = input('Insira o nome: ')


def imprime_nome(nome='Jon Doe'):
    print('+----+', '+' + '-' * len(nome) + '+')
    print('|Olá|', '', '|{}|'.format(nome))
    print('+----+', '+' + '-' * len(nome) + '+')


imprime_nome(nome_usuario)
