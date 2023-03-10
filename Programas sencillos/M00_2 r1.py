# El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

# 1. Asegurate de que devuelve la cadena original
# 2. Utiliza la función específica de python para resolverlo

# Retos

# 1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.
# 2. Hazlo sin utilizar la función específica de python


cadena = input("Introduzca la cadena de caracteres que desea: ")
while cadena == "":
    cadena = input("No deje su cadena vacía. Escríbala de nuevo: ")
length_cadena = len(cadena)


print(f"Su cadnea tiene un número de caracteres de: {length_cadena}")
