// # El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

// # 1. Asegurate de que devuelve la cadena original
// # 2. Utiliza la función específica de python para resolverlo

// # Retos

// # 1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.
// # 2. Hazlo sin utilizar la función específica de python

let str = prompt("Introduzca la cadena de caracteres que desea: ");
let cadena = str;
let contador = 0;

while (cadena !== "") {
    cadena = cadena.substring(1);
    contador++;
}

console.log(`Su cadena '${str}' tiene un número de ${contador} caracteres`);