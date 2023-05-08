// # # Solucionando problemas del coche
// # # Hacer un programa que siga el siguiente arbol de decisiones para dar con el diagnóstico del problema de nuestro coche.


// # # Por ejemplo:

// # # ¿Arranca? S
// # # ¿Suena un clic-clic? S

// # # Entonces:
// # # Reemplaza la batería
// # # Restricciones
// # # Realiza las preguntas relevantes según las respuestas del usuario
// # # Retos
// # # Investigar sobre árboles de decisión y como codificarlo sin hacerlo a capón como arriba

let respuesta = prompt("¿Arranca?");
let solucion = "Todo parece OK";

if (respuesta.toLowerCase() === "s") {
  respuesta = prompt("¿Suena un clic-clic?");
  if (respuesta.toLowerCase() === "s") {
    solucion = "Reemplaza la batería";
  } else {
    respuesta = prompt("¿Se enciende el coche pero no arranca?");
    if (respuesta.toLowerCase() === "s") {
      solucion = "Revisa las bujías";
    } else {
      respuesta = prompt("¿Arranca el coche y luego se cala?");
      if (respuesta.toLowerCase() === "s") {
        respuesta = prompt("¿Es un coche de inyección?");
        if (respuesta.toLowerCase() === "s") {
          solucion = "Lleve el coche al taller";
        } else {
          solucion = "Abra y cierre el starter";
        }
      }
    }
  }
} else {
  respuesta = prompt("¿Están los bornes de la batería corroidos?");
  if (respuesta.toLowerCase() === "s") {
    solucion = "Limpia los bornes y arranca de nuevo";
  } else {
    solucion = "Reemplaza los cables y arranca de nuevo";
  }
}

console.log(`Entonces...\n${solucion}`);