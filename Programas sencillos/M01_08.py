# # Modulo de estadísticas de un texto

# Crear un módulo con las siguientes funciones

# - contarCaracteres(texto)
# - contarPalabras(texto)
# - contarVocales(texto)
# - contarConsonantes(texto)

# ## Restricciones
# - Cada función devolverá el valor numérico de lo que cuenta.
# - Si el módulo se ejecuta directamente (sin ser importado por otro programa deberá listar todos los valores de un texto en forma de tabla tabulada)

def contarCaracteres(texto):
  return len(texto)

def contarPalabras(texto):
  return len(texto.split())

def contarVocales(texto):
  vocales = 0
  for caracter in texto:
    if caracter in 'aeiouAEIOU':
      vocales +=1
  
  return vocales

def contarConsonantes(texto):
  consonantes = 0
  for caracter in texto:
    if caracter in('bcdfghjklmnñpqrstuvwxyzBCDFGHJKLMNÑPQRSTUVWXYZ'):
      consonantes += 1
  return consonantes


if __name__ == '__main__':
  texto = input("Introduce un texto, por favor: ")
  
  print("Caracteres.: {:5d}".format(contarCaracteres(texto)))
  print("Palabras...: {:5d}".format(contarPalabras(texto)))
  print("Vocales....: {:5d}".format(contarVocales(texto)))
  print("Consonantes: {:5d}".format(contarConsonantes(texto)))