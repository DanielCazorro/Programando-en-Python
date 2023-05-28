# Ejercicio 7. Aproximación a pi

# Enunciado
# Una forma de aproximarse al valor de pi es sumar cuantos más términos mejor de la siguiente secuencia:
# 𝜋=3+42⋅3⋅4−44⋅5⋅6+46⋅7⋅8−48⋅9⋅10+... 
# Construye un programa que presente las primeras 15 aproximaciones del número, para que se vea como se va acercando. Consideraremos la primera aproximación la primera suma.
# 3+42⋅3⋅4 
# Debes mostrar el resultado de esta y de 14 iteraciones más, cada una en su línea.

# FIXME: Hay que arreglar la lógica
def approxiamtionPi():
    """
    Presenta las 15 primeras aproximaciones de pi
    """
    piList = []
    counter = 0
    operation = (4/((2+ counter) * ( 3+counter) *  (4+ counter)))

    index = 1

    for number in range(1,15):
        number = 3
        if index % 2 != 0:
            number += operation
        else:
            number -=  operation
        piList.append(number)
        counter +=2
        index += 1

    print (piList)
    return piList

approxiamtionPi()