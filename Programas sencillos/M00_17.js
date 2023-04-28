// # Conversor de temperatura
// # Crear un programa que convierta temperatura de Fahrenheita a Celsius y viceversa. El programa pedirá que tipo de conversión queremos y la mostrará.

// # Las fórmulas de conversión son:

// # C = (F−32)⋅59

// # F = (C⋅95)+32

// # Restricciones
// # Se puede elegir el tipo de conversión en mayúsculas o minúsculas
// # Reducir el número de sentencias al mínimo y no repetir prints
// # Retos
// # Asegurar que las entradas son numéricas
// # Modificar el programa para que acepte grados Kelvin

// # Toma de datos

const tipo = prompt("Introduzca la temperatura a convertir (Celsius/Fahrenheit): ");
let temperatura_inicial = prompt("Valor de la temperatura: ");
temperatura_inicial = parseFloat(temperatura_inicial);

let temperatura_final, nombre_final;

if (tipo.toUpperCase() === "CELSIUS") {
    temperatura_final = (temperatura_inicial * (9 / 5)) + 32;
    nombre_final = "Fahrenheit";
} else if (tipo.toUpperCase() === "FAHRENHEIT") {
    temperatura_final = (temperatura_inicial - 32) * (5 / 9);
    nombre_final = "Celsius";
} else {
    console.log("Ha introducido una temperatura incorrecta");
}

console.log(`Sus ${temperatura_inicial} grados ${tipo} equivalen a: ${temperatura_final} grados ${nombre_final}`);

