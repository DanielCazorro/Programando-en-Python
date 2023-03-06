// Introducción de datos
dia = parseInt(prompt("Día: "))
mes = parseInt(prompt("Mes: "))

//  Contar los días
contador_dias = 0
if (mes == 1) {
    contador_dias = dia
}
else if (mes == 2) {
    contador_dias = 31 + dia
}
else if (mes == 3) {
    contador_dias = 31 + 28 + dia
}
else if (mes == 4) {
    contador_dias = 31 + 28 + 31 + dia
}
else if (mes == 5) {
    contador_dias = 31 + 28 + 31 + 30 + dia
}
else if (mes == 6) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + dia
}
else if (mes == 7) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + dia
}
else if (mes == 8) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia
}
else if (mes == 9) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia
}
else if (mes == 10) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia
}
else if (mes == 11) {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia
}
else {
    contador_dias = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia
}

alert("Es el día: " + contador_dias)