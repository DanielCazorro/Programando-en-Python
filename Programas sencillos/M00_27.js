// # # Calculando la media

// # Crear un programa que calcule la media de un conjunto de valores introducido por el usuario. Si el usuario entra 0 (cero) se considerará el final de la entrada de valores y se procederá a calcular la media. 

// # ## Restricciones

// # 1. El cero no se debe incluir en el cálculo de la media
// # 2. Si el primer valor introducido es un cero el programa mostrará un mensaje de error
// # 3. Mantener separadas la entrada, salida y proceso dentro del programa.
// # 4. Si el valor introducido no es numérico volver a pedirlo


function floatValue(n) {
    try {
      let resultado = parseFloat(n);
      if (isNaN(resultado)) {
        throw "Not a Number";
      }
      return resultado;
    } catch {
      return null;
    }
  }
  
  let total = 0;
  let contador = 0;
  let numero = null;
  
  while (numero !== 0) {
    let strNumero = prompt("Introduce valor:");
    numero = floatValue(strNumero);
    
    while (numero === null) {
      console.log(`${strNumero} debe ser un número`);
      strNumero = prompt("Introduce valor:");
      numero = floatValue(strNumero);
    }
    
    total += numero;
    contador++;
  }
  
  if (contador === 1) {
    console.log("No se han introducido valores");
  } else {
    let media = total / (contador - 1);
    console.log(`Media = ${total}/${contador-1} = ${media}`);
  }
  