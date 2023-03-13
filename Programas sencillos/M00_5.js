// # # Operaciones aritméticas

// # Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

// # # Restricciones

// # 1. Convertir las cadenas de entrada en números
// # 2. Separar convenientemente la entrada, transformación de cadena en números y salida separados
// # 3. Crea una única sentencia de salida con los saltos de línea adecuados(sólo un print)

// # Pedir datos
const uno = prompt("Introduzca el primer número: ")
const dos = prompt("Introduzca el segundo número: ")
intUno = parseInt(uno)
intDos = parseInt(dos)

// # Operaciones
suma = intUno + intDos
resta = intUno - intDos
producto = intUno * intDos
division = intUno / intDos

// # Resultados

alert(
    `Las operaciones de los números ${intUno} y ${intDos} son:\nSuma: ${suma}\nResta: ${resta}\nProducto: ${producto}\nDivision: ${division}`)


// # OTRA FORMA DE HACERLO EN MENOS LINEAS

// # strOp1 = input("Introduce un número: ")
// # strOp2 = input("Introduce un segundo número:")

// # op1 = float(strOp1)
// # op2 = float(strOp2)

// # print("{} + {} = {}\n{} - {} = {}\n{} · {} = {}\n{} / {} = {}\n".format(op1,
// #       op2, op1+op2, op1, op2, op1-op2, op1, op2, op1*op2, op1, op2, op1/op2))
