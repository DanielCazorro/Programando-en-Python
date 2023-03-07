dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def es_bisiesto(year):
    if year % 4 != 0:
        # if not year % 4 == 0: ESTA CONDICIÓN ES IGUAL A LA SUPERIOR
        return False

    if year % 100 == 0 and year % 400 != 0:
        # if not year % 100 != 0 and not year % 400 == 0: ESTA CONDICIÓN ES IGUAL A LA SUPERIOR
        return False

    return True


# Pedir datos
dia = int(input("Día: "))
mes = int(input("Mes: "))
anyo = int(input("Año: "))

# Comprobar bisiesto

if es_bisiesto(anyo):
    dias[1] = 29

# Contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while compara_mes < mes - 1:
    contador_dias += dias[compara_mes]
    compara_mes += 1

contador_dias += dia

print("El día es: ", contador_dias)
