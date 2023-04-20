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

cantidad_invertida = 0
while cantidad_invertida == 0:
    cantidad_invertida = input("Cantidad invertida: ")
    try:
        P = float(cantidad_invertida)
        if P <= 0:
            print("Debe introducir un número mayor que cero")
            cantidad_invertida = 0
    except:
        print("Debe introducir un número válido")
        cantidad_invertida = 0

interes = "ERROR"
while interes == "ERROR":
    interes = input("Interés: ")
    try:
        r = float(interes) / 100
    except:
        print("Debe introducir un número válido")
        interes = "ERROR"

anios = 0
while anios == 0:
    anios = input("Años transcurridos: ")
    try:
        t = int(anios)
        if t <= 0:
            print("Debe introducir una fecha positiva y mayor que cero")
            anios = 0
    except:
        print("Debe introducir un valor válido")
        anios = 0


# Cálculos

A = P * (1 + r*t)

cantidad_ganada = A

cantidad_anual = A/t

# Muestra de resultados

print(f"Durante {anios} años, cada año ganará: {cantidad_anual} € \nTras {anios} años de inversión al {interes} %, su cantidad debe ser: {cantidad_ganada:.2f} €")
