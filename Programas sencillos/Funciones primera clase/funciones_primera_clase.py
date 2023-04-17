def voz_alta(texto):
    return texto.upper() + "!!!"


def voz_baja(texto):
    return chr(129323) + texto.lower()


gritando = voz_alta
susurrando = voz_baja


def saludar(saludo):
    print('*' * len(saludo))
    print(saludo)
    print('.' * len(saludo))
