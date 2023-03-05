// Pedimos el nombre
let nombre = prompt("¿Cómo te llamas? ")
alert("Hola", nombre)

//  Pedimos la edad y la convertimos a int
edad = prompt("¿Cuántos años tienes? ")

//  Pedimos el año actual y lo convertimos a int
a_actual = prompt("¿En qué año estamos? ")

has_cumplido = prompt("¿Has cumplido años ya (S/N)? ")

//  Realizamos el cálculo
if (has_cumplido === "S") {
    a_nacimiento = a_actual - edad
}
else {
    a_nacimiento = (a_actual - edad) - 1
}
//  Mostramos el resultado
alert(nombre, "naciste en", a_nacimiento)