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

# Datos
bote = 5
tasa_conversion = 0.05

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

# Operaciones
superficie = ancho * alto

litros_necesarios = superficie * tasa_conversion

if litros_necesarios % bote == 0:
    botes_necesarios = int(litros_necesarios / bote)
else:
    botes_necesarios = int((litros_necesarios // bote) + 1)

# Datos

print(f"Necesitarás {litros_necesarios} litros para pintar {superficie} metros cuadrados de techo.\nDebes comprar {botes_necesarios} botes de pintura")
