ano_admissao = int(input('Digite o ano da sua admissão: '))
ano_atual = int(input('Digite o ano atual: '))
salario = float(input('Insira seu salário: '))
tempo_de_empresa = ano_atual - ano_admissao

if (tempo_de_empresa >= 5):
    print('Sua bonificação será de {}'.format(salario * 0.2))
else:
    print('Sua bonificação será de {}'.format(salario * 0.1))
