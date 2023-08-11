qnt_dias = int(input("Quantos dias? "))
qnt_horas = int(input("Quantas horas? "))
qnt_minutos = int(input("Quantos minutos? "))
qnt_segundos = int(input("Quantos segundos? "))

qnt_tempo_segundos = (
    qnt_dias * 24 * 60 * 60 + qnt_horas * 60 * 60 + qnt_minutos * 60
    + qnt_segundos
)

print("Total de tempo em segundos: {}".format(qnt_tempo_segundos))
