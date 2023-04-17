ALFABETO = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')


def cesar(caracter, clave):
    posicion = ALFABETO.index(caracter)
    nposicion = posicion + clave
    nposicion = nposicion % len(ALFABETO)
    return ALFABETO[nposicion]
