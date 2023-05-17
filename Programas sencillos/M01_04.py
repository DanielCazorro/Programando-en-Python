# Centrar cadena en terminal

# Crear una función que añada espacios por delante a una cadena hasta dejarla centrada en la terminal. Para ello se utilizarán como parámetros la cadena y la anchura en caracteres del terminal.
# Restricciones

# No se deben añadir espacios por detrás de la cadena

# Retos
# Controlar que los parámetros son del tipo adecuado, es decir, cadena es un string y anchura un entero. Utilizando la documentación de python podemos ver que se puede validar el tipo de una variable utilizando la funcion predefinida isinstance() ver aquí

def center(cadena, anchura):
  resultado = "ERROR"
  if isinstance(cadena, str) and isinstance(anchura, int):
    lonEspacios = (anchura - len(cadena)) // 2
    resultado = lonEspacios * ' ' + cadena
  else:
    resultado = "ERROR"

  return resultado
  
print(center('HEY', 25))