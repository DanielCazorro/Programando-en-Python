# # Determinar el precio de un conjunto de entradas al Zoo

# Hacer un programa que muestre el precio total de las entradas de un grupo de personas al zoo. Teniendo en cuenta los siguientes precios:

# - niños de 2 o menos años: no pagan
# - Hasta los 12 años: 14 €
# - Jubilados de 65 o más año: 18€
# - Resto: 23€.

# El programa pedirá la edad de los componentes del grupo, primero pedirá una edad, y sucesivamente las demás. En el momento en que se introduzca un 0 se considerará el final y el programa devolverá lo siguiente:

# ```
# 1 entradas de baby (0€):      0.00€
# 3 entradas de menores (14€): 42.00€
# 2 entradas normales (23€):   46.00€
# 1 entradas jubilado (18€):   18.00€
#                              ------
#                             106.00 €
# ```

def cost(age):
    age = int(age)
    if age <= 2:
        price = 0
    elif age > 2 and age < 12:
        price = 14
    elif age >= 65:
        price = 18
    else:
        price = 23

    return price

def totalPrice():

    age = -1
    total = 0

    while age != "0":
        age = -1
        age = input("Introduzca la edad o 0 para terminar: ")
        total += cost(age)

    print(f"Coste total: {total}")
    return total

totalPrice()