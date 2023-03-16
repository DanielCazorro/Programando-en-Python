// # # Repartiendo pizza

// # Escribir un programa que sabiendo cuantas personas hay en una reunión y cuantas pizzas se han comprado, queriendo que cada persona tenga una porción de cada pizza.
// # La pizza sólo puede dividirse en un número par de porciones

// # ```
// # ¿Número de personas? 7
// # ¿Número de pizzas? 3

// # 7 personas con 3 pizzas
// # Cada persona toma 3 piezas
// # Sobran 3 porciones
// # ```
// # Retos

// # 1. Asegurar que la entrada es numerica, positiva y entera. En otro caso impedir que el usuario continue


// # Datos:
let pizza = 0;
while (pizza <= 0) {
    try {
        pizza = prompt("¿Cuántas pizzas se han comprado?: ");
        pizza = parseInt(pizza);
    } catch {
        console.log("Debe introducir un número entero y positivo de pizzas.");
        pizza = 0;
    }
}

let personas = 0;
while (personas <= 0) {
    try {
        personas = prompt("¿Cuántas personas hay?: ");
        personas = parseInt(personas);
    } catch {
        console.log("Debe introducir un número entero y positivo de personas.");
        personas = 0;
    }
}

// Operaciones:
let porciones;
if (personas % 2 === 1) {
    porciones = personas + 1;
} else {
    porciones = personas;
}

let sobrante = (porciones * pizza) % personas;

// Resultados:
console.log(`Hay ${personas} personas y ${pizza} pizzas.\nCada persona toma ${pizza} porciones.\nSobran ${sobrante} porciones`);