# De número a mes
# Hacer un programa que traduzca los números del 1 al 12 a los meses del año. Hacerlo con if - elif .

# Restricciones
# Dejar una única instrucción de salida
# Retos
# Sustituir la selección con una estructura de datos complejos
# Hacer el mismo programa en más de un idioma(a elegir por el usuario)

dict_meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
              7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

num_mes = int(input("Introduzca el número del mes deseado: "))

print(f"{dict_meses[num_mes]}")
