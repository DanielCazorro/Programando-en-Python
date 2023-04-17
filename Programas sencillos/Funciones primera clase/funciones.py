def voz_alta(texto):
    return texto.upper() + "!!!"


def voz_baja(texto):
    return chr(129323) + texto.lower()


print(voz_alta("Hola"))
print(voz_baja("Adios"))


gritando = voz_alta
susurrando = voz_baja

print(gritando("Hola"))
print(susurrando("Adios"))
