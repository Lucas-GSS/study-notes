# Pagamento à vista – conceder desconto de 5%;
# Pagamento em 3x – o valor não sofre alterações;
# Pagamento em 5x – acréscimo de 2%;
# Pagamento em 10x – acréscimo 8%.

print(
    "FORMAS DE PAGAMENTO",
    "1- À Vista (5% de desconto)",
    "2- 3x (valor não altera)",
    "3- 5x (acréscimo de 2%)",
    "4- 10x (acréscimo 8%)",
    "5- Sair",
    sep="\n",
)

valor_produto = float(input("Valor do produto: "))
forma_pagamento = int(input("Forma de pagamento: "))

if forma_pagamento == 1:
    print("À vista: {} R$".format(valor_produto - valor_produto * 0.05))
elif forma_pagamento == 2:
    print('Parc. 3x: {}R$'.format(valor_produto))
elif forma_pagamento == 3:
    print('Parc. 5x: {}R$'.format(valor_produto + valor_produto * 0.02))
elif forma_pagamento == 4:
    print('Parc. 10x: {}R$'.format(valor_produto + valor_produto * 0.08))
else:
    print('Operação encerrada. Até mais.')
