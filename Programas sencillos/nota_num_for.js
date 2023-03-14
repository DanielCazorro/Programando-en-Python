const nota_numerica = (letra) => {
    const letras = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"];
    const notas = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0];
    let puntero = 0;

    while (letras[puntero] !== letra) {
        puntero++;
    }

    return notas[puntero];
};

const pedir_nota_correcta = () => {
    let valor = "";

    while (valor === "") {
        const nota = prompt("Nota: ").toUpperCase();

        try {
            valor = nota_numerica(nota);
        } catch (error) {
            console.log(`Nota ${nota} incorrecta. Vuelva a introducir.`);
            valor = "";
        }
    }

    return valor;
};

const pedir_numero = () => {
    let valor = "";

    while (valor === "") {
        try {
            valor = parseInt(prompt("Número de asignaturas: "));
        } catch (error) {
            console.log("Debe ser un número entero. Vuelva a introducirlo.");
            valor = "";
        }
    }

    return valor;
};

const num_notas = pedir_numero();
let sum_notas = 0;

for (let i = 0; i < num_notas; i++) {
    const valor = pedir_nota_correcta();

    sum_notas += valor;
}

if (num_notas === 0) {
    console.log("No se han introducido datos.");
} else {
    const media = sum_notas / num_notas;
    console.log(`La media es: ${media}`);
}