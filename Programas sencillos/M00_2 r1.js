// # El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

// # 1. Asegurate de que devuelve la cadena original
// # 2. Utiliza la función específica de python para resolverlo

// # Retos

// # 1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.
// # 2. Hazlo sin utilizar la función específica de python


const cadena = prompt("Introduzca la cadena de caracteres que desea: ");
while (cadena === "") {
    cadena = prompt("No deje su cadena vacía. Escríbala de nuevo: ");
}
const length_cadena = cadena.length;

console.log(`Su cadena tiene un número de caracteres de: ${length_cadena}`);
alert(`Su cadena tiene un número de caracteres de: ${length_cadena}`);