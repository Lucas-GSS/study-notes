nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media_aluno = (nota1 + nota2 + nota3) / 3

if (media_aluno >= 7):
    print('Média final: {}. Aprovado!'.format(media_aluno.__round__(2)))
else:
    print('Média final: {}. Reprovado!'.format(media_aluno.__round__(2)))
