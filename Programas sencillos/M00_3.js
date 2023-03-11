// # # Imprimiendo comillas

// # Construir un programa que pida una cita y un autor y devuelva una única cadena con la cita entre comillas y el autor.

// # ## Restricciones

// # 1. No usar format ni % ni fstring.Hacerlo concatenando cadenas y escapando caracteres

const cita = prompt("Escriba la cita deseada: ")
const autor = prompt("Escriba el autor de su cita: ")

alert("La cita:'" + cita + "', pertenece al autor:'" + autor + "'.")
console.log("La cita: '" + cita + "', pertenece al autor: '" + autor + "'.")


// # ESTA ES OTRA FORMA CORRECTA A LA SUPERIOR

// const cita = prompt("Introduce una frase famosa, por favor: ")
// const autor = prompt("¿Quien es su autor? ")

// const output = '\'' + cita + '\', ' + autor
// console.log(output)
