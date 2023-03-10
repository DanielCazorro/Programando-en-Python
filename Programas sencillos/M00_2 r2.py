# El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

# 1. Asegurate de que devuelve la cadena original
# 2. Utiliza la función específica de python para resolverlo

# Retos

# 1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.
# 2. Hazlo sin utilizar la función específica de python


str = input("Introduzca la cadena de caracteres que desea: ")
cadena = str
contador = 0

while cadena != "":
    cadena = cadena[1:]
    contador += 1

print("Su cadena '{}' tiene un número de {} caracteres".format(str, contador))
