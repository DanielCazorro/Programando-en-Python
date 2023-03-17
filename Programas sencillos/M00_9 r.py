# Pintando el techo
# 5 litros de pintura dan para pintar 100 metros cuadrados de techo. Teniendo esto en cuenta haz un programa que diga cuantos botes de 5 litros de pintura hay que comprar para pintar un techo de anchura y profundidad informada por el usuario(en metros). Devuelve el número de botes suficiente y por supuesto en números enteros.

# Necesitarás 12 litros para pintar 240 metros cuadrados de techo.

# Debes comprar 3 botes de pintura.
# Restricciones
# Utiliza una constante para calcular la conversión botes de pintura/metros de techo
# Asegurate de comprar un número entero de botes de pintura suficiente(el siguiente número entero) pero no de más
# Retos
# Revisar que la entrada sean números positivos. Si no es así no dejar que el usuario continue
# Hacer el cálculo para habitación redonda
# Hacer el cálculo para habitación en forma de L

import math

# Datos
bote = 5
tasa_conversion = 0.05

tipo_habitacion = ""
while tipo_habitacion.lower() not in ("1", "2", "3"):
    tipo_habitacion = input(
        "Rectangular = 1\nRedondo = 2\nEn forma de L = 3\nEscriba el número correspondiente a tipo de techo: ")

if tipo_habitacion == "1":
    ancho = 0
    while ancho <= 0:
        try:
            ancho = input("Introduzca el ancho del techo en metros: ")
            ancho = float(ancho)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            ancho = 0

    alto = 0
    while alto <= 0:
        try:
            alto = input("Introduzca el alto del techo en metros: ")
            alto = float(alto)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            alto = 0

elif tipo_habitacion == "2":
    radio = 0
    while radio <= 0:
        try:
            radio = input("Introduzca el radio del techo en metros: ")
            radio = float(radio)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            radio = 0

else:
    ancho_1 = 0
    while ancho_1 <= 0:
        try:
            ancho_1 = input(
                "Introduzca el ancho de la parte inferior de la habitación: ")
            ancho_1 = float(ancho_1)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            ancho_1 = 0

    alto_1 = 0
    while alto_1 <= 0:
        try:
            alto_1 = input("Introduzca el alto del techo inferior en metros: ")
            alto_1 = float(alto_1)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            alto_1 = 0

    ancho_2 = 0
    while ancho_2 <= 0:
        try:
            ancho_2 = input(
                "Introduzca el ancho de la parte superior de la habitación: ")
            ancho_2 = float(ancho_2)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            ancho_2 = 0

    alto_2 = 0
    while alto_2 <= 0:
        try:
            alto_2 = input("Introduzca el alto del techo superior en metros: ")
            alto_2 = float(alto_2)
        except:
            print("Debe introducir un número válido, positivo y mayor que cero")
            alto_2 = 0


# Operaciones
if tipo_habitacion == "1":
    superficie = ancho * alto

elif tipo_habitacion == "2":
    superficie = math.pi * radio ** 2

else:
    superficie1 = alto_1 * ancho_1
    superficie2 = alto_2 * ancho_2
    superficie = superficie1 + superficie2

litros_necesarios = superficie * tasa_conversion

if litros_necesarios % bote == 0:
    botes_necesarios = int(litros_necesarios / bote)
else:
    botes_necesarios = int((litros_necesarios // bote) + 1)

# Datos

print(f"Necesitarás {litros_necesarios:.2f} litros para pintar {superficie:.2f} metros cuadrados de techo.\nDebes comprar {botes_necesarios} botes de pintura")
