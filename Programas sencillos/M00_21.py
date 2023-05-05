# Máximo valor
# Introduce 3 números y muestra el mayor

# Restricciones
# Impedir continuar si no son números
# Impedir continuar si no son todos distintos
# Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor.
# Retos
# Intentar hacerlo de manera más eficiente con funciones y estructuras de datos
# Modificar el programa para hacerlo con 10 números
# Modificar el programa para hacerlo con tantos números como el usuario quiera

# Toma de datos
n1 = "N"
while n1 == "N":
    n1 = input("Primer número: ")
    try:
        float(n1)
    except:
        print("Debe introducir un valor numérico.")
        n1 = "N"

n2 = "N"
while n2 == "N":
    n2 = input("Segundo número: ")
    try:
        float(n2)
        if n2 == n1:
            print("Debe ser un número diferente al anterior")
            n2 = "N"
    except:
        print("Debe introducir un valor numérico.")
        n2 = "N"

n3 = "N"
while n3 == "N":
    n3 = input("Tercer número: ")
    try:
        float(n3)
        if n3 == n2:
            print("Debe ser un número diferente al anterior")
            n3 = "N"
        if n3 == n1:
            print("Debe ser un número diferente al anterior")
            n3 = "N"
    except:
        print("Debe introducir un valor numérico.")
        n3 = "N"

if n1 > n2 and n1 > n3:
    nmax = n1
elif n2 > n1 and n2 > n3:
    nmax = n2
else:
    nmax = n3

print(f"El mayor número de todos es: {nmax}")
