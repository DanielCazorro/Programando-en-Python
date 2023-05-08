// # Máximo valor
// # Introduce 3 números y muestra el mayor

// # Restricciones
// # Impedir continuar si no son números
// # Impedir continuar si no son todos distintos
// # Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor.
// # Retos
// # Intentar hacerlo de manera más eficiente con funciones y estructuras de datos
// # Modificar el programa para hacerlo con 10 números
// # Modificar el programa para hacerlo con tantos números como el usuario quiera

// # Toma de datos
let n1 = "N";
while (n1 === "N") {
  n1 = prompt("Primer número: ");
  try {
    parseFloat(n1);
  } catch {
    console.log("Debe introducir un valor numérico.");
    n1 = "N";
  }
}

let n2 = "N";
while (n2 === "N") {
  n2 = prompt("Segundo número: ");
  try {
    parseFloat(n2);
    if (n2 === n1) {
      console.log("Debe ser un número diferente al anterior");
      n2 = "N";
    }
  } catch {
    console.log("Debe introducir un valor numérico.");
    n2 = "N";
  }
}

let n3 = "N";
while (n3 === "N") {
  n3 = prompt("Tercer número: ");
  try {
    parseFloat(n3);
    if (n3 === n2) {
      console.log("Debe ser un número diferente al anterior");
      n3 = "N";
    }
    if (n3 === n1) {
      console.log("Debe ser un número diferente al anterior");
      n3 = "N";
    }
  } catch {
    console.log("Debe introducir un valor numérico.");
    n3 = "N";
  }
}

let nmax;
if (n1 > n2 && n1 > n3) {
  nmax = n1;
} else if (n2 > n1 && n2 > n3) {
  nmax = n2;
} else {
  nmax = n3;
}

console.log(`El mayor número de todos es: ${nmax}`);