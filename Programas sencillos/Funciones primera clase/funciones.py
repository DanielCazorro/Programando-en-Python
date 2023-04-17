def voz_alta(texto):
    return texto.upper() + "!!!"


def voz_baja(texto):
    return chr(129323) + texto.lower()


gritando = voz_alta
susurrando = voz_baja

dialogo = [
    ('Hola', gritando),
    ('Por favor, no chilles, me duele mucho la cabeza', None),
    ('Perdona, ¿quieres una aspirina?', voz_baja)
]

for frase, modo in dialogo:
    if modo == None:
        print(frase)
    else:
        print(modo(frase))
