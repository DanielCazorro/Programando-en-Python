# Indice de masa corporal
# Craer un programa que calcule el indice de masa corporal de una persona según la fórmula

# IMC = pesoaltura2

# Si el índice de masa corporal está entre 18, 5 y 15 el peso se considera normal. Por encima se considera sobrepeso, por debajo delgadez.

# Haz un programa que pida ambos datos, devuelva tu índice de masa corporal e indique si estás por encima o por debajo de la normalidad

# Restricciones
# Impedir que el programa continúe si se introducen datos no numéricos

# Retos
# Crear una versión que acepte unidades de altura y peso anglosajonas(deberás buscar y cambiar la fórmulas)
# Partiendo de la siguiente tabla
# Clasificación	IMC
# Delgadez Severa < 16, 00
# Delgadez Moderada	16, 00 - 16, 99
# Delgadez leve	17, 00 - 18, 49
# Normal	18, 50 - 25, 00
# Preobeso	25, 01 - 29, 99
# Obesidad leve	30, 00 - 34, 99
# Obesidad media	35 - 39, 99
# Obesidad mórbida >= 40
# Devolver el diagnóstico según el imc.

# Toma de datos

peso = "OFF"
while peso == "OFF":
    peso = input("Introduzca su peso en KG: ")
    try:
        peso = float(peso)
        if peso <= 0:
            print("Debe introducir un valor positivo.")
            peso = "OFF"
    except:
        print("Debe introducir valores numérico.")
        peso = "OFF"

altura = "OFF"
while altura == "OFF":
    altura = input("Introduzca su altura en metros: ")
    try:
        altura = float(altura)
        if altura <= 0:
            print("Debe introducir un valor positivo y mayor que cero.")
            altura = "OFF"
    except:
        print("Debe introducir un valor numérico.")
        altura = "OFF"

# Cálculos

IMC = peso / (altura**2)

if IMC < 15:
    masa = "Delgadez"
elif IMC >= 15 and IMC < 18:
    masa = "Normal"
else:
    masa = "Sobrepeso"

print(
    f"Su índice de masa corporal es de: {IMC}\nPor lo tanto, se encuentra en un estado de: {masa}")
