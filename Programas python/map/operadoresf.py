def voz_alta(texto):
    return texto.upper() + "!!!"


def voz_baja(texto):
    return chr(129323) + texto.lower()


frutas = ["plátano", "plátano", "fresa",
          "naranja", "uva", "uva", "fresa", "plátano"]

lfConAsterisco = list(map(lambda p: '*' + p + '*', frutas))
lMayusculas = list(map(voz_alta, frutas))

print(lfConAsterisco)
print(lMayusculas)

lMayusculasIterando = []

for fruta in frutas:
    lMayusculasIterando.append(voz_alta(fruta))

print(lMayusculasIterando)
