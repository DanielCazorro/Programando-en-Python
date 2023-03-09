// # Hola, mundo
// # Hacer un programa que pida el nombre y te salude por tu nombre

// # Restricciones
// # Mantener entrada, salida y concatenación separados

// # Retos
// # Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.

nombre = prompt("¿Cuál es tu nombre?: ")

if (nombre == "Daniel") {
    alert("Hola, " + nombre + ". Encantado de concerte.")
}
else if (nombre == "Pedro") {
    alert("Ey, " + nombre + ", ¿cómo te va?")
}
else if (nombre == "Susana") {
    alert("Buenas tardes " + nombre + ".Es hora de trabajar.")
}
else {
    alert("Que la fuerza te acompañe " + nombre)
}
