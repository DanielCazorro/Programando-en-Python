# # Ejercicio 3. Sin repeticiones

# ## Enunciado

# Necesitamos una función que recibirá una lista con 6 elementos (cadenas o números) y devolverá la misma lista sin repeticiones. Con los elementos en el orden original


def returning(listOfChains):
    """
    Recibe una lista y devuelve la misma lista sin repeticiones
    """
    finalList = []

    for chain in listOfChains:
        if not chain in finalList:
            finalList.append(chain)
    return finalList

print(returning([1,2,3,1,5,5,7,1,2]))