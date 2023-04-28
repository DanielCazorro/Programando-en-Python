# Conversor de temperatura
# Crear un programa que convierta temperatura de Fahrenheita a Celsius y viceversa. El programa pedirá que tipo de conversión queremos y la mostrará.

# Las fórmulas de conversión son:

# C = (F−32)⋅59

# F = (C⋅95)+32

# Restricciones
# Se puede elegir el tipo de conversión en mayúsculas o minúsculas
# Reducir el número de sentencias al mínimo y no repetir prints
# Retos
# Asegurar que las entradas son numéricas
# Modificar el programa para que acepte grados Kelvin

# Toma de datos

tipo = input(
    "Introduzca la temperatura a convertir (Celsius/Fahrenheit): ")
temperatura_inicial = "ERROR"
while temperatura_inicial == "ERROR":
    temperatura_inicial = input("Valor de la temperatura: ")
    try:
        temperatura_inicial = float(temperatura_inicial)
    except:
        print("Debe introducir una valor numérico")
        temperatura_inicial = "ERROR"

if tipo.upper() == "CELSIUS":
    temperatura_final = (temperatura_inicial * (9/5)) + 32
    nombre_final = "Fahrenheit"
elif tipo.upper() == "FAHRENHEIT":
    temperatura_final = (temperatura_inicial-32) * (5/9)
    nombre_final = "Celsius"
else:
    print("Ha introducido una temperatura incorrecta")

print(f"Sus {temperatura_inicial} grados {tipo} equivalen a: {temperatura_final:.2f} grados {nombre_final}")
