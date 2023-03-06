dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Pedir datos
dia = int(input("Día: "))
mes = int(input("Mes: "))

# Contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while compara_mes < mes - 1:
    contador_dias += dias[compara_mes]
    compara_mes += 1

contador_dias += dia

print("El día es: ", contador_dias)
