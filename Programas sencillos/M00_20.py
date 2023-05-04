# De número a mes
# Hacer un programa que traduzca los números del 1 al 12 a los meses del año. Hacerlo con if - elif .

# Restricciones
# Dejar una única instrucción de salida
# Retos
# Sustituir la selección con una estructura de datos complejos
# Hacer el mismo programa en más de un idioma(a elegir por el usuario)


num_mes = int(input("Introduzca el número del mes deseado: "))

if num_mes == 1:
    mes = "Enero"
elif num_mes == 2:
    mes = "Febrero"
elif num_mes == 3:
    mes = "Marzo"
elif num_mes == 4:
    mes = "Abril"
elif num_mes == 5:
    mes = "Mayo"
elif num_mes == 6:
    mes = "Junio"
elif num_mes == 7:
    mes = "Julio"
elif num_mes == 8:
    mes = "Agosto"
elif num_mes == 9:
    mes = "Septiembre"
elif num_mes == 10:
    mes = "Octubre"
elif num_mes == 11:
    mes = "Noviembre"
elif num_mes == 12:
    mes = "Diciembre"
else:
    mes = "Desconocido"

print(mes)
