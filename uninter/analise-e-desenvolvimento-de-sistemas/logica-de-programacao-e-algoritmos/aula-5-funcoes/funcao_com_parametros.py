# Uma função pode receber valores externos à ela para processar.
# Esses dados são fornecidos à função por meio de parâmetros
# Um parâmetro pode ter um valor padrão, o que faz dele opcional
# Caso contrário, ele é obrigatório para o funcionamento correto da função


def hello(nome='Jon Doe'):
    print('Olá, {}!'.format(nome))


hello('Lucas')
hello()
