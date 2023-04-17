def voz_alta(texto):
    return texto.upper() + "!!!"


def voz_baja(texto):
    return chr(129323) + texto.lower()


frutas = ["platano", "platano", "fresa",
          "naranja", "uva", "uva", "fresa", "platano", ""]

lfConAsterisco = list(map(lambda p: '*' + p + '*', frutas))
lMayusculas = list(map(voz_alta, frutas))

print(lfConAsterisco)
print(lMayusculas)

lMayusculasIterando = []

for fruta in frutas:
    lMayusculasIterando.append(voz_alta(fruta))

print(lMayusculasIterando)


lp3aletraA = list(filter(lambda p: len(p) > 2 and p[2] == 'a', frutas))


def es3A(p):
    return len(p) > 2 and p[2] == 'a'


lp3aletraAF = list(filter(es3A, frutas))

print(lp3aletraA)
print(lp3aletraAF)
