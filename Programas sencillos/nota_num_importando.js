import * as mis_funciones from "./mis_funciones.js";

const num_notas = mis_funciones.pedir_numero();
let sum_notas = 0;

for (let i = 0; i < num_notas; i++) {
    const valor = mis_funciones.pedir_nota_correcta();

    sum_notas += valor;
}

if (num_notas === 0) {
    console.log("No se han introducido datos");
} else {
    const media = sum_notas / num_notas;
    console.log(`La media es: ${media}`);
}