// # Tabla de multiplicar
// # Crear un programa que escriba la tabla de multiplicar del número introducido por el usuario, así

// # Introduzca valor: 5

// # 5 x 1 = 5
// # 5 x 2 = 10
// # 5 x 3 = 15
// # 5 x 4 = 20
// # 5 x 5 = 25
// # 5 x 6 = 30
// # 5 x 7 = 35
// # 5 x 8 = 40
// # 5 x 9 = 45
// # 5 x 10 = 50
// # Restricciones
// # El programa debe impedir la entrada de cualquier número que no sea entero y positivo y volverá a pedirlo
// # Retos
// # Formatear la tabla para que los valores salgan en columnas y ajustados a la derecha.
// # Seguir pidiendo valores hasta que el usuario introduzca un 0 (cero) entonces parar
// # Plantear solución con while y con for

let valor = 0;
while (valor <= 0) {
  valor = prompt("Introduzca un valor positivo y mayor que cero: ");
  try {
    valor = parseInt(valor);
  } catch (error) {
    console.log("Debe introducir un valor numérico");
    valor = 0;
  }
}

let start_valor = valor;

for (let number = 1; number <= 10; number++) {
  console.log(`${start_valor} x ${number} = ${valor}`);
}