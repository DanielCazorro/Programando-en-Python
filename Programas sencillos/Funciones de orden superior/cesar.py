ALFABETO = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')


def cesar(caracter, clave):
    posicion = ALFABETO.index(caracter)
    nposicion = posicion + clave
    return ALFABETO[nposicion]
