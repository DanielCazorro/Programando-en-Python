def tacha(caracter, palabra):
    lpalabra = list(palabra)
    lpalabra.remove(caracter)
    return ''.join(lpalabra)


def es_anagrama(p1, p2):
    for letra in p1:
        if letra in p2:
            p2 = tacha(letra, p2)
        else:
            return False

    return p2 == ""
