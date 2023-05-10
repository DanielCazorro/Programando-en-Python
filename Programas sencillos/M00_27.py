# # Calculando la media

# Crear un programa que calcule la media de un conjunto de valores introducido por el usuario. Si el usuario entra 0 (cero) se considerará el final de la entrada de valores y se procederá a calcular la media. 

# ## Restricciones

# 1. El cero no se debe incluir en el cálculo de la media
# 2. Si el primer valor introducido es un cero el programa mostrará un mensaje de error
# 3. Mantener separadas la entrada, salida y proceso dentro del programa.
# 4. Si el valor introducido no es numérico volver a pedirlo

def floatValue(n):
  try:
    resultado = float(n)
  except:
    resultado = None
  return resultado

total = 0
contador = 0
numero = None

while numero != 0:
    strNumero = input("Introduce valor: ")
    numero = floatValue(strNumero)
    while numero == None:
      print ("{} debe ser un número".format(strNumero))
      strNumero = input("Introduce valor: ")
      numero = floatValue(strNumero)
    total = total + numero
    contador = contador + 1

if contador == 1:
  print("No se han introducido valores")
else:
  media = total / (contador - 1)
  print("Media = {}/{} = {}".format(total, contador-1, media))

