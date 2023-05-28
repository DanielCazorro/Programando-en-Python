# Ejercicio 1. Elementos de una sucesión menores o iguales a 100

## Enunciado

# Crea las funciones que devuelvan las listas con los elementos de las siguientes sucesiones que sean menores o iguales a 100. Utiliza para ello sólo range.

# - Primera sucesión: 1, 4, 7, 10, 13,...
# - Segunda sucesión: -12, -7, -2, 3, 8,...

def successions(start, step):
    """
    Crea una lista de números, desde inicio hasta 100, que sumen 
    de step en step
    """
    finalList = []
    for numer in range(start, 100, step):
        finalList.append(numer)

    return finalList

print(successions(-8,10))