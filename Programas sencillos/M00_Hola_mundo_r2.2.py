# Hola, mundo
# Hacer un programa que pida el nombre y te salude por tu nombre

# Restricciones
# Mantener entrada, salida y concatenación separados

# Retos
# Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.

nombre = input("¿Cuál es tu nombre?: ")

if nombre == "Daniel":
    print(f"Hola, {nombre}. Es un placer conocerte.")
elif nombre == "Pedro":
    print(f"Ey, {nombre}, ¿cómo te va?")
elif nombre == "Susana":
    print(f"Buenas tardes {nombre}. Es hora de trabajar.")
else:
    print(f"Que la fuerza te acompañe {nombre}")
