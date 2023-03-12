def nota_numerica(letra):
    letras = ['A+', 'A', 'A-', 'B+', 'B',
              'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]

    puntero = 0

    while letras[puntero] != letra:
        puntero += 1

    return notas[puntero]


num_notas = 0
sum_notas = 0

nota = input("Escriba la nota o deje en blanco para terminar: ")

while nota != "":
    try:
        valor_nota = nota_numerica(nota)
        num_notas += 1
        sum_notas += valor_nota
    except IndexError:
        print("Nota", nota, "es incorrecta. Vuelva a intentarlo")

    nota = input("Escriba la nota o deje en blanco para terminar: ")

media = sum_notas / num_notas

print(f"La nota media es: {media}")
