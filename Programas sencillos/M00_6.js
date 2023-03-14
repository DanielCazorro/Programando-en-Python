// # # Cálculo de la jubilación

// # Incorpora el año actual al programa. Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año en que te jubilarás. Algo así

// # ```
// # ¿Cuantos años tienes? 48
// # ¿A qué edad te jubilarás? 67
// # Te quedan 19 años para jubilarte
// # Estamos en 2018, te jubilarás en 2037.
// # ```
// # # Restricciones

// # 1. Convertir las cadenas de entrada en números
// # 2. Obten el año actual como lo haga python(no vale ponerlo como constante en el programa)
// # Es necesario importar las depencendias necesarias

// Importamos las dependencias necesarias
const now = new Date();
const year_actual = now.getFullYear();

let edad_jubilacion = 0;
while (edad_jubilacion === 0) {
    try {
        edad_jubilacion = prompt("Introduzca la edad a la que se va a jubilar: ");
        edad_jubilacion = parseInt(edad_jubilacion);
    } catch {
        console.log("Debe introducir una edad de jubilación válida.");
        edad_jubilacion = 0;
    }
}

let edad = 0;
while (edad === 0) {
    try {
        edad = prompt("Introduzca su edad: ");
        edad = parseInt(edad);
    } catch {
        console.log("Debe introducir una edad válida");
        edad = 0;
    }
}

// Cálculos
const years_para_jubilacion = edad_jubilacion - edad;
const year_jubilacion = year_actual + years_para_jubilacion;

// Resultado
if (edad >= edad_jubilacion) {
    console.log(`Locura total!! Ya te puedes jubilar.Tienes ${edad} años, y podías jubilarte a los ${edad_jubilacion}.Así que ve buscando viajes que es hora de disfrutar.`);
} else {
    console.log(`Te quedan ${years_para_jubilacion} para jubilarte\nEstamos en ${year_actual}, te jubilarás en ${year_jubilacion}`);
}
