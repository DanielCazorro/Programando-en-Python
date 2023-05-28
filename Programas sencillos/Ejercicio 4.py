# Ejercicio 4. Por debajo, en y por encima de la media

# Enunciado
# Crea una función que de una lista de 6 números enteros, separe en tres listas los números que están por debajo, por encima y son iguales a la media (si hay alguno) y que mantenga el orden de entrada

def numbers(listOfNumbers):
    """
    Divide la lista en tres diferentes, dependiendo si son iguales
    superiores o inferiores a la media
    """

    media = 0
    hightList = []
    lowList = []
    sameList = []


    for number in listOfNumbers:
        media += number
    
    media = media / 6

    for number in listOfNumbers:
        if number < media:
            lowList.append(number)
        elif number > media:
            hightList.append(number)
        else:
            sameList.append(number)
    
    print(f"Mayores que la media: {hightList}\nMenores que la media: {lowList}\nIguales a la media: {sameList}")
    return hightList, lowList, sameList

numbers([1,2,1,0,1,1])
