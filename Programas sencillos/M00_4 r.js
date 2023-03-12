// # # Concatenando cadenas

// # Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

// # # Restricciones

// # 1. Utilizar un solo print en el programa
// # 2. Hacer una versión utilizando substitucion

// # Retos

// # 1. Introducir más datos para complicar y aumentar la historia
// # 2. Construye una historia del estilo de los libros de * Construye tu propia aventura * de forma que la historia derive según se elija una u otra opción.

const nombre = prompt("Escriba un nombre: ")
const verbo = prompt("Escriba un verbo: ")
const adverbio = prompt("Escriba un adverbio: ")
const adjetivo = prompt("Escriba un adjetivo: ")



const nombre2 = prompt("Introduzca otro nombre: ")
const verbo2 = prompt("Escriba otro verbo: ")
const adverbio2 = prompt("Escriba otro adverbio: ")
const adjetivo2 = prompt("Escriba otro adjetivo: ")

alert(
    `Esta es la historia del ${adjetivo} ${nombre}. Su mayor virtud era poder ${verbo} ${adverbio} toda la noche. De repente vio dos puertas, con los números 41 y 22.`)

let camino = "";
while (camino !== '22' && camino !== '41') {
    camino = prompt("¿Por que puerta pasarás(22/41)?")
}
if (camino === '41') {
    console.log(
        `Al pasar por la puerta vio un ${adjetivo2} gato llamado ${nombre2}. Ese gato iba a ${verbo} ${adverbio} cuando de repente todo se volvió negro y despertaste del sueño.`)
}
else if (camino === '22') {
    console.log(
        `Una ráfaga de aire frío pasó a tu alrededor, y viste una forma ${adjetivo2} que se hacía llamar ${nombre2}. Mientras te contaba que le gustaba ${verbo2} ${adverbio2} te iba arrastrando al pozo, del que nunca saldrás.`)
}