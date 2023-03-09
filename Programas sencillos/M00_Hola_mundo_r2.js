// # Hola, mundo
// # Hacer un programa que pida el nombre y te salude por tu nombre

// # Restricciones
// # Mantener entrada, salida y concatenación separados

// # Retos
// # Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.

const saludos = ["Hola,", "Encantado", "Un placer conocerte", "Mucho gusto"]

const nombre = prompt("¿Cuál es tu nombre?")

const saludo = Math.floor(Math.random() * 4)

console.log(saludos[saludo] + " " + nombre)
alert(saludos[saludo] + " " + nombre)
