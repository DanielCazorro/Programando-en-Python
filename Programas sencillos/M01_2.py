# # Fortaleza de una contraseña

# Crea un programa que dtermine la complejidad de una contraseña en base a las siguientes reglas:

# 1. Una contraseña muy débil contiene sólo números y su longitud es menor de 8 carácteres
# 2. Una contraseña  débil contiene sólo letras y su longitud es menor de 8 carácteres
# 3. Una contraseña es fuerte si contiene letras y al menos un número y tiene al menos 8 carácteres de longitud
# 4. Una contraseña es muy fuerte si tiene letras, números y caracteres especiales con al menos 8 carácteres de longitud

# ## Restricciones

# 1. Crear una función `validaPwd` que devuelva un valor que evaluado por otro programa determine si la contraseña es muy débil, débil, fuerte o muy fuerte. No devuelvas una cadena, debe servir para otros lenguajes.
# 2. Utilizar una sentencia de salida única

letters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ " #Incluyo el espacio como letra pos si se admiten frases como pwd
numbers = "0123456789"

def veryWeakIndicator(pwd):
  res = False
  if len(pwd) < 8:
    res = True
    for i in range(0, len(pwd)):
      res = res and pwd[i] in numbers
  
  return res

def weakIndicator(pwd):
  res = False
  if len(pwd) < 8:
    res = True
    for i in range(0, len(pwd)):
      res = res and (pwd[i] in letters or pwd[i] in numbers) #He decidido que si es menor de 8 con letras y números es igual que menos de 8 letras

  return res

def strongIndicator(pwd):
  res = False
  leastOneNumber = 0
  if len(pwd) >= 8:
    res = True
    for i in range(0, len(pwd)):
      swNumber = pwd[i] in numbers
      leastOneNumber += 1 if swNumber else 0
      res = res and (pwd[i] in letters or swNumber)

  return res and leastOneNumber > 0

def veryStrongIndicator(pwd):
  res = False
  if len(pwd) >= 8:
    swNumbers = swLetters = swOthers = False
    for i in range(0, len(pwd)):
      swNumbers = True if pwd[i] in numbers else swNumbers
      swLetters = True if pwd[i] in letters else swLetters
      swOthers = True if pwd[i] in numbers else swOthers
    return swNumbers and swLetters and swOthers

  return res

def validaPwd(pwd):
  if veryStrongIndicator(pwd):
    return 3
  elif strongIndicator(pwd):
    return 2
  elif weakIndicator(pwd):
    return 1
  elif veryWeakIndicator(pwd):
    return 0
  else:
    return -1
  