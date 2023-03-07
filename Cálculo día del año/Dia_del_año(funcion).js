dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

function esBisiesto(year) {
    if (year % 4 != 0) {
        return false
    }

    if (year % 100 == 0 && year % 400 != 0) {
        return false
    }

    return true
}

// Pedir datos
dia = parseInt(prompt("Día: "))
mes = parseInt(prompt("Mes: "))
anyo = parseInt(prompt("Año: "))

if (esBisiesto(anyo)) {
    dias[1] = 29
}

//  Contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while (compara_mes < mes - 1) {
    contador_dias += dias[compara_mes]
    compara_mes += 1
}

contador_dias += dia

alert("Día del año: " + contador_dias)
