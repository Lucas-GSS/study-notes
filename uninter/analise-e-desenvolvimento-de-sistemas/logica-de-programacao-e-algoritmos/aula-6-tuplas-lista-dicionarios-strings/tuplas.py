# Tupla é uma estrutura de dados que armazena conjuntos de valores de forma
# sequencial. Uma vez definido os valores, eles não podem ser alterados
# durante a execução do programa. A tupla não suporta reatribuição de valores.
# Se um dos valores for uma lista, os itens da lista podem ser alterados

tupla = ("Lucas Gabiel", 23, "MG", "Developer")

# gera o erro de atribuição
# tupla[0] = 'Angus'

for item in tupla:
    print(item)

top_10_linguagens = (
    "Rust",
    "TypeScript",
    "Python",
    "Kotlin",
    "Go",
    "Julia",
    "Dart",
    "C#",
    "JavaScript",
    "SQL"
)

print('Top 10 linguagens: \n')

for i in range(len(top_10_linguagens)):
    print('{}- {}'.format(i+1, top_10_linguagens[i]))

print('Top 3: ')
print(top_10_linguagens[:3])

print('5 últimas: ')
print(top_10_linguagens[4:-1])

posicao_python = top_10_linguagens.index('Python') + 1

print('Python está na {}ª posição'.format(posicao_python))

# A tupla pode ser usada como parâmetro de funções, quando o número
# de parâmetros for variável:


def printa_o_maior(msg, *numeros):
    maior = 0
    for i in range(0, len(numeros), 1):
        if (numeros[i] > maior):
            maior = numeros[i]
    print(msg, maior)


printa_o_maior('Maior: ', 1, 5, 7, 3, 2)
