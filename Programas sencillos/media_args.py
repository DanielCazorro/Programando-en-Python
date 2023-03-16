from mis_funciones import nota_numerica


def media(*notas):
    suma_notas = 0
    for nota in notas:
        valor_nota = nota_numerica(nota)
        suma_notas += valor_nota

    if len(notas) > 0:
        return suma_notas / len(notas)


def multientrada(*valores):
    for valor in valores:
        print(valor * 2)
