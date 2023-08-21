# Função é um bloco de código que executa uma rotina específica.
# Seu objetivo é organizar o código e torná-lo reutilizável.
# Podem ser chamadas de procedimento, caso não retornem nada.
# Um código divido em funções é um código modularizado.
# Assim ele é reutilizável, mais legível e mais fácil de manter e testar


usuarios = []


def registrador():
    nome = input('Insira o nome: ')
    usuarios.append(nome)


qnt_de_registros = int(input('Quantos usuários deseja inserir? '))


for i in range(qnt_de_registros):
    registrador()

print('Usuários inseridos: {}'.format(usuarios))
