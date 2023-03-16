// # # Area de un rectángulo

// # Pide la entrada del ancho y profundo de la habitación en metros. Devuelve la superficie en metros cuadrados y en yardas cuadradas (tomando la referencia de [aquí](https://es.wikipedia.org/wiki/Sistema_anglosaj%C3%B3n_de_unidades)).

// # ## Restricciones

// # 1. Mantener los cálculos separados de la salida
// # 2. Usa una constante para las conversiones de unidades ([aquí](https://es.wikipedia.org/wiki/Sistema_anglosaj%C3%B3n_de_unidades))

// # Retos

// # 1. Fuerza a que las entradas sean numéricas. Si no son numericas el usuario no podrá continuar.
// # 2. Crea una versión del programa que permita elegir si la entrada va en metros o en yardas

// # Datos
eleccion = prompt("Eliga metros o yardas")

let ancho = 0;
while (ancho <= 0) {
    try {
        ancho = parseFloat(
            prompt("Introduzca el ancho. Debe ser un valor positivo y numérico: "));
    } catch {
        ancho = 0;
    }
}

let profundidad = 0;
while (profundidad <= 0) {
    try {
        profundidad = parseFloat(
            prompt("Introduzca la profundidad. Debe ser un valor positivo y numérico: "));
    } catch {
        profundidad = 0;
    }
}

// Operaciones
const tasa_yarda = 0.83612736;
const superficie = ancho * profundidad;

if (eleccion.toLowerCase() === 'metros') {
    const superficie_yardas = superficie / tasa_yarda;
    console.log(
        `La superficie en ${eleccion} cuadrados será: ${superficie} y en yardas cuadradas será: ${superficie_yardas}`);
} else {
    const superficie_yardas = superficie * tasa_yarda;
    console.log(
        `La superficie en ${eleccion} cuadradas será: ${superficie} y en yardas cuadradas será: ${superficie_yardas}`);
}