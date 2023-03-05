// Calcular el porcentaje de retención para el IRPF en función de mi sueldo y circunstancias

//  Obtención de datos
sueldo = prompt("Sueldo: ")
situacion = prompt("Situación (1/2/3) ")
num_hijos = prompt("Número de hijos: ")

//  Calcular exención
exencion = 0

if (situacion == '1') {
    if (num_hijos <= 0) {
        exencion = 0
    }
    else if (num_hijos == 1) {
        exencion = 17270
    }
    else {
        exencion = 18617
    }
}

if (situacion == '2') {
    if (num_hijos <= 0) {
        exencion = 16696
    }
    else if (num_hijos == 1) {
        exencion = 17894
    }
    else {
        exencion = 19241
    }
}

if (situacion == '3') {
    if (num_hijos <= 0) {
        exencion = 15000
    }
    else if (num_hijos == 1) {
        exencion = 15599
    }
    else {
        exencion = 16272
    }
}

sueldo_a_retener = sueldo - exencion

//  Obtener retencion

if (sueldo_a_retener <= 12450) {
    porcentaje = 19
}
else if (sueldo_a_retener <= 20199) {
    porcentaje = 24
}
else if (sueldo_a_retener <= 35199) {
    porcentaje = 30
}
else if (sueldo_a_retener <= 59999) {
    porcentaje = 37
}
else if (sueldo_a_retener <= 299999) {
    porcentaje = 45
}
else {
    porcentaje = 47
}

monton_anual = sueldo_a_retener * porcentaje / 100
monto_mensual = monton_anual / 12

//  Mostramos resultados
alert("Sueldo anual: \t", sueldo)
alert("Situación: \t", situacion)
alert("Base a retener: \t", sueldo_a_retener)
alert("Porcentaje: \t", porcentaje)
alert("Total anual: \t", monton_anual)
alert("Retención mensual: \t", monto_mensual)