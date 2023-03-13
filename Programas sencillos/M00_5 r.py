# # Operaciones aritméticas

# Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

# # Restricciones

# 1. Convertir las cadenas de entrada en números
# 2. Separar convenientemente la entrada, transformación de cadena en números y salida separados
# 3. Crea una única sentencia de salida con los saltos de línea adecuados(sólo un print)

# Retos
# Controla que las entradas sean números de forma que el programa no avance si no se introduce un número
# No permitas introducir números negativos

# Pedir datos
uno = ""

while not isinstance(uno, int):
    uno = input("Introduzca el primer número: ")
    try:
        uno = int(uno)
        if uno <= 0:
            print("Debe introducir un número positivo.")
            uno = ""
    except:
        print("Debe introducir un número válido.")
        uno = ""

dos = ""
while not isinstance(dos, int):
    dos = input("Introduzca el segundo número: ")
    try:
        dos = int(dos)
        if dos <= 0:
            print("Debe introducir un número positivo.")
            dos = ""
    except:
        print("Debe introducir un número válido.")
        dos = ""


# Operaciones
suma = uno + dos
resta = uno - dos
producto = uno * dos
division = uno / dos

# Resultados

print(
    f"Las operaciones de los números {uno} y {dos} son:\nSuma: {suma}\nResta: {resta}\nProducto: {producto}\nDivision: {division}")


# OTRA FORMA DE HACERLO EN MENOS LINEAS

# strOp1 = input("Introduce un número: ")
# strOp2 = input("Introduce un segundo número:")

# op1 = float(strOp1)
# op2 = float(strOp2)

# print("{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(op1,
#       op2, op1+op2, op1, op2, op1-op2, op1, op2, op1*op2, op1, op2, op1/op2))
