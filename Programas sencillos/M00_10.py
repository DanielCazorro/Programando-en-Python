# Aplicando impuestos
# Haz un programa que aplique un impuesto de 5, 5 % sobre tres precios introducidos por el usuario. Deben introducirse también el número de ejemplares de producto de cada precio que se compran. Se debe imprimir el subtotal sin tasas, la tasa y la suma de ambos

# Restricciones
# Manten separadas las partes de entrada, salida y proceso de tu programa
# Retos
# Comprobar que la entrada sea numérica e impedir continuar si no es así
# Permitir que el programa tenga un número indeterminado de productos y cantidades de entrada

# Entrada
impuesto = 0.55

precio1 = 0
while precio1 <= 0:
    precio1 = input("Introduzca el primer precio: ")
    try:
        precio1 = float(precio1)
        if precio1 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        precio1 = 0

ejemplares1 = 0
while ejemplares1 <= 0:
    ejemplares1 = input(
        "Introduzca el número de ejemplares del primer producto: ")
    try:
        ejemplares1 = int(ejemplares1)
        if ejemplares1 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        ejemplares1 = 0

precio2 = 0
while precio2 <= 0:
    precio2 = input("Introduzca el segundo precio: ")
    try:
        precio2 = float(precio2)
        if precio2 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        precio2 = 0

ejemplares2 = 0
while ejemplares2 <= 0:
    ejemplares2 = input(
        "Introduzca el número de ejemplares del segundo producto: ")
    try:
        ejemplares2 = int(ejemplares2)
        if ejemplares2 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        ejemplares2 = 0

precio3 = 0
while precio3 <= 0:
    precio3 = input("Introduzca el tercer precio: ")
    try:
        precio3 = float(precio3)
        if precio3 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        precio3 = 0

ejemplares3 = 0
while ejemplares3 <= 0:
    ejemplares3 = input(
        "Introduzca el número de ejemplares del tercer producto: ")
    try:
        ejemplares3 = int(ejemplares3)
        if ejemplares3 <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido.")
        ejemplares3 = 0

# Operaciones
subtotal = 0
subtotal += precio1*ejemplares1
subtotal += precio2*ejemplares2
subtotal += precio3*ejemplares3

tasa = subtotal * impuesto

total = subtotal + tasa

# Datos

print(f"\nSubtotal: {subtotal}\nTasas: {tasa:.2f}\nTotal: {total}")
