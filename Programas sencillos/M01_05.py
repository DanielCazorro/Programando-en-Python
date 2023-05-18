# Crear funcion que convierta un texto a minúsculas
# Crear funcion que convierta un texto a minúsculas según la definición myLower(cadena)

# Restricciones
# Crearla de tal manera que sólo incluya los caracteres alfabéticos
# Crearla en forma de módulo (más detalles aquí)

mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def minusculas(cadena):
  res = ""
  for caracter in cadena:
    if caracter in mayusculas:
      res += chr(ord(caracter)+32)
    else:
      res += caracter
  return res