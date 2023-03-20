# Conversión de divisas
# Crear un programa que pase de dolares a euros. El programa pedirá la tasa de cambio de dolares a euros(cuantos euros se necesitan para tener un dolar). El programa debe devolver lo siguiente

# X dolares a una tasa de cambio de Y
# Total €

# Restricciones
# Asegúrate de que la entrada se redondea al centavo
# Utiliza una única sentencia de salida

# Retos
# Crea un diccionario de tasas de conversión y pregunta por paises, no por monedas.

# Entrada
dolares = 0
while dolares <= 0:
    dolares = input("Introduzca los dólares a convertir: ")
    try:
        dolares = float(dolares)
        if dolares <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido")
        dolares = 0
dolares = round(dolares, 2)

tasa = 0
while tasa <= 0:
    tasa = input("Introduzca la tasa de conversión a euros: ")
    try:
        tasa = float(tasa)
        if tasa <= 0:
            print("Debe introducir un número positivo mayor que cero.")
    except:
        print("Debe introducir un número válido")
        tasa = 0

# Operación
eur = dolares * tasa

print(f"\n{dolares} dólares a una tasa de cambio de {tasa:.2f}\nTotal: {eur:.2f}")
