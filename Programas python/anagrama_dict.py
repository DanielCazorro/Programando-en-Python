
def frecuencias(palabra):
    resultado = {}
    for letra in palabra:
        if letra in resultado:
            resultado[letra] += 1
        else:
            resultado[letra] = 1


def es_anagrama_dict(p1, p2):
    return frecuencias(p1) == frecuencias(p2)
