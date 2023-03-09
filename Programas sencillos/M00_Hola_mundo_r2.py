# Hola, mundo
# Hacer un programa que pida el nombre y te salude por tu nombre

# Restricciones
# Mantener entrada, salida y concatenación separados

# Retos
# Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.

import random
saludos = ("Hola,", "Encantado ", "Un placer conocerte", "Mucho gusto")

nombre = input("¿Cuál es tu nombre?: ")

saludo = random.randint(0, 3)

print(saludos[saludo], nombre)
