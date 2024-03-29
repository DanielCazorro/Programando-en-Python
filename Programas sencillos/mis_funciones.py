def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B',
              'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]

    puntero = 0
    letra = letra.upper()

    while letras[puntero] != letra:
        puntero += 1

    return notas[puntero]


def pedir_nota_correcta():
    valor = ""
    while valor == "":
        nota = input("Nota: ").upper()

        try:
            valor = nota_numerica(nota)
        except IndexError:
            print(f"Nota {nota} incorrecta. Vuelva a introducir.A")
            valor = ""

    return valor


def pedir_numero():
    valor = ""
    while valor == "":
        try:
            valor = int(input("Número de asignautras: "))
        except ValueError:
            print("Debe ser un número entero. Vuelva a introducirlo.")
            valor = ""
    return valor
