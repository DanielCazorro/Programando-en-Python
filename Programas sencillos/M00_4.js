// # # Concatenando cadenas

// # Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

// # # Restricciones

// # 1. Utilizar un solo print en el programa
// # 2. Hacer una versión utilizando substitucion

const nombre = prompt("Escriba un nombre: ")
const verbo = prompt("Escriba un verbo: ")
const adverbio = prompt("Escriba un adverbio: ")
const adjetivo = prompt("Escriba un adjetivo: ")

console.log(
    `Esta es la historia del ${adjetivo} ${nombre}. Su mayor virtud era poder ${verbo} ${adverbio} toda la noche.`)
