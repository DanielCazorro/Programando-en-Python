# # Cálculo de la jubilación

# Incorpora el año actual al programa. Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año en que te jubilarás. Algo así

# ```
# ¿Cuantos años tienes? 48
# ¿A qué edad te jubilarás? 67
# Te quedan 19 años para jubilarte
# Estamos en 2018, te jubilarás en 2037.
# ```
# # Restricciones

# 1. Convertir las cadenas de entrada en números
# 2. Obten el año actual como lo haga python(no vale ponerlo como constante en el programa)
# Es necesario importar las depencendias necesarias

# Importamos las dependencias necesarias
from datetime import datetime

# Fecha actual
now = datetime.now()
year_actual = now.year

edad_jubilacion = 0
while edad_jubilacion == 0:
    try:
        edad_jubilacion = input(
            "Introduzca la edad a la que se va a jubilar: ")
        edad_jubilacion = int(edad_jubilacion)
    except:
        print("Debe introducir una edad de jubilación válida.")
        edad_jubilacion = 0

edad = 0
while edad == 0:
    try:
        edad = input("Introduzca su edad: ")
        edad = int(edad)
    except:
        print("Debe introducir una edad válida")
        edad = 0

# Cálculos

years_para_jubilacion = edad_jubilacion - edad
year_jubilacion = year_actual + years_para_jubilacion


# Resultado:
if edad >= edad_jubilacion:
    print(
        f"Locura total!! Ya te puedes jubilar. Tienes {edad} años, y podías jubilarte a los {edad_jubilacion}. Así que ve buscando viajes que es hora de disfrutar. ")
else:
    print(
        f"Te quedan {years_para_jubilacion} para jubilarte\nEstamos en {year_actual}, te jubilarás en {year_jubilacion} ")
