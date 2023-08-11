valor_produto = int(input('Insira o valor do produto: '))
desconto = int(input('Insira o valor do desconto: '))
valor_final = valor_produto - (valor_produto * (desconto / 100))
print('O valor com desconto aplicado é: {}'.format(valor_final))
