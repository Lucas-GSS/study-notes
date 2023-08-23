def validar_string(string, min, max):
    tamanho = len(string)
    if (tamanho < min or tamanho > max):
        return True
    else:
        return False


texto = input('Digite um texto de 3 a 15 caracteres: ')

while validar_string(texto, 3, 15):
    texto = input('Digite um texto de 3 a 15 caracteres: ')


print(texto)
