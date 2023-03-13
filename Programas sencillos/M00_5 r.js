// # # Operaciones aritméticas

// # Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

// # # Restricciones

// # 1. Convertir las cadenas de entrada en números
// # 2. Separar convenientemente la entrada, transformación de cadena en números y salida separados
// # 3. Crea una única sentencia de salida con los saltos de línea adecuados(sólo un print)

// # Retos
// # Controla que las entradas sean números de forma que el programa no avance si no se introduce un número
// # No permitas introducir números negativos

// # Pedir datos
uno = ""

while (typeof uno !== "number") {
    uno = prompt("Introduzca el primer número: ")
    try {
        uno = parseInt(uno)
        if (uno <= 0) {
            alert("Debe introducir un número positivo.")
            uno = ""
        }
    } catch {
        alert("Debe introducir un número válido.")
    }
}

dos = ""
while (typeof dos !== "number") {
    dos = prompt("Introduzca el segundo número: ")
    try {
        dos = parseInt(dos)
        if (dos <= 0) {
            alert("Debe introducir un número positivo.")
            dos = ""
        }
    } catch {
        alert("Debe introducir un número válido.")
        dos = ""
    }
}


// # Operaciones
suma = uno + dos
resta = uno - dos
producto = uno * dos
division = uno / dos

// # Resultados

alert(
    `Las operaciones de los números ${uno} y ${dos} son:\nSuma: ${suma}\nResta: ${resta}\nProducto: ${producto}\nDivision: ${division}"`)

