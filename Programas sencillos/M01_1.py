# Anagramas
# Crear un programa que indique si una cadena es un anagrama de otra (mismos carácteres en orden diferente). Ejemplo

# Primera cadena: otra
# Segunda cadena: rota

# "otra" y "rota" son anagramas
# Restricciones
# Hacerlo con la función esAnagrama
# Ambas palabras deben tener la misma longitud
# Reto
# Hacerlo sin las facilidades de manejo de cadenas de python

def is_anagram(word1, word2):
  if len(word1) != len(word2):
    print('False')
    return False 

  listword2 = list(word2)
  for letter in range(0, len(word1)):
    print(listword2)
    for letter2 in range(0, len(word2)):
      if word1[letter] == listword2[letter2]:
        listword2[letter2] = '*'
        break
  
  print(listword2)
        
  comp = '*'*len(word2)
  word2 = "".join(listword2)
  print(comp, 'vs', word2)
  print('True')
  return comp == word2


def is_anagram2(word1, word2):
  if len(word1) != len(word2):
    print('False')
    return False 
  
  position = []

  for i in range(0, len(word1)):  
    print(position)
    for j in range(0, len(word2)):
      if word1[i] == word2[j] and j not in position:
        position.append(j)
  
  print(position)
  print('True')
  return len(position) == len(word2)

is_anagram('otra', 'arto')
is_anagram2('reto', 'oer')