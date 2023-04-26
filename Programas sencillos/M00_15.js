// # // Validando contraseñas
// # // Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden.En el caso de que lo hagan devolver un mensaje Entró en el sistema y en el contrario No te conozco, no pasas

// # // Lo interesante de este programa no es sólo la estructura de if necesarias, sino también la estructura de datos necesaria para almacenar usuarios y sus contraseñas.

// # //     Restricciones
// # // Utilizar if/else
// # // Hacer el programa sensible a mayúsculas - minúsculas
// # // Retos
// # // Impide que la contraseña se vea.Investiga para ello
// # // Utiliza un diccionario en lugar de una tupla de tuplas
let lista_usuarios = { "Pedro": "peDrito123", "Juan": "32Juaniii" };

let entrada_usuario = prompt("Introduzca su usuario:");
let entrada_contrasenia = prompt("Introduzca su contraseña:");

if (entrada_contrasenia === lista_usuarios[entrada_usuario]) {
    console.log("Entró en el sistema");
} else {
    console.log("No te conozco, no pasas");
}
