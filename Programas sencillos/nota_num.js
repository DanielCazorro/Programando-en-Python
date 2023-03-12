function notaNumerica(letra) {
    letras = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F']
    notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]

    puntero = 0

    while (letras[puntero] != letra && puntero < letras.length) {
        puntero += 1
    }

    if (puntero == letras.length) {
        throw new Error("Nota" + letra + "inexistente")
    }
    return notas[puntero]
}


numNotas = 0
sumNotas = 0

nota = prompt("Nota o vacío para acabar")

while (nota != "") {
    if (nota != null) {
        nota = nota.toUpperCase()
    }


    try {
        valorNota = notaNumerica(nota)
        numNotas += 1
        sumNotas += valorNota
    } catch (e) {
        alert("Nota " + nota + " no es correcta. Vuelve a intentarlo.")
    }

    nota = prompt("Nota o vacío para acabar")
}

if (numNotas == 0) {
    alert("No se han introducido datos")
} else {
    media = sumNotas / numNotas
    alert("La media es: " + media)
}
