// Entrada
let dolares = 0;
while (dolares <= 0) {
    dolares = prompt("Introduzca los dólares a convertir: ");
    try {
        dolares = parseFloat(dolares);
        if (dolares <= 0) {
            console.log("Debe introducir un número positivo mayor que cero.");
        }
    } catch {
        console.log("Debe introducir un número válido");
        dolares = 0;
    }
}
dolares = Math.round(dolares * 100) / 100;

let tasa = 0;
while (tasa <= 0) {
    tasa = prompt("Introduzca la tasa de conversión a euros: ");
    try {
        tasa = parseFloat(tasa);
        if (tasa <= 0) {
            console.log("Debe introducir un número positivo mayor que cero.");
        }
    } catch {
        console.log("Debe introducir un número válido");
        tasa = 0;
    }
}

// Operación
let eur = dolares * tasa;

console.log(`${dolares} dólares a una tasa de cambio de ${tasa.toFixed(2)}`);
console.log(`Total: ${eur.toFixed(2)}`);