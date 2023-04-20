"""
Cálculo de interés simple
Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

A = P⋅(1+rt)

donde A es la cantidad ganada, P la cantidad invertida, r el interes y t los años transcurridos desde el inicio de la inversión

Tras X años de inversión al Y %, su cantidad debe ser T
Restricciones
La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0, 15
La inversión debe redondearse al céntimo
La salida debe formatearse como divisa(€)
Retos
Valida que las entradas sean numéricas y que el usuario no pueda continuar si no introduce un número
Modifica el programa para que imprima el valor de la inversión cada año de la misma hasta llegar al valor pedido
"""
# Toma de datos

cantidad_invertida = input("Cantidad invertida: ")
P = float(cantidad_invertida)

interes = input("Interés: ")
r = float(interes) / 100

anios = input("Años transcurridos: ")
t = int(anios)

# Cálculos

A = P * (1 + r*t)

cantidad_ganada = A

# Muestra de resultados

print(f"Tras {anios} años de inversión al {interes} %, su cantidad debe ser: {cantidad_ganada:.2f} €")
