# # Ejercicio 5. Extraer dígitos de un número cualquiera

# ## Enunciado

# Basándote en la solución del ejercicio 7 del bloque de booleanos, que juega con cociente y resto de la división entre potencias de 10 para sacar los tres dígitos de un número de tres cifras. Construye una función que te devuelva una lista ordenada con los dígitos de un número entero ignorando su signo talque:
# - `digitos(2837) -> [2, 8, 3, 7]`
# `

def digits(number):
    """
    Devuelve los dígitos de un número entero
    """
    finalList = list(str(number))
    numberfinalList = []

    for number in finalList:
        numberInt = int(number)
        numberfinalList.append(numberInt)

    print (numberfinalList)
    return numberfinalList


digits(2837)