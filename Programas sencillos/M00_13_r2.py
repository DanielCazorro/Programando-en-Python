# Calculando el interés compuesto
# Introduciremos aquí los exponentes. En préstamos o inversiones a largo plazo se suele utilizar más el interes compuesto que el simple(diferencias entre ambos). Se trata ahora de escribir un programa que calcule el interés compuesto sobre un capital a lo largo del tiempo.

# El programa ha de pedir el capital inicial, el interes anual, el número de años de la inversión y el número de veces que se calcula en interés en el año. La fórmula a aplicar es:

# A = P(1+rn)nt

# donde

# P es el capital inicial
# r el interes anual
# t los años que dura la inversión(o préstamo)
# n el número de veces que se acumula el interés por año(por ejemplo 12 si es mensual)
# A es la cantidad al final de la inversión,
# Así, para:

# 1500 € de capital inicial
# 4, 3 % de interes
# 6 años de duración del préstamo
# Se calcula el interés al trimestre(4 periodos por año)
# El programa debería devolver

# 1500.00 € invertidos al 4.3 % durante 6 años con 4 periodos de imposición por año se transforman en 1938.84 €
# Restricciones
# El interés se introduce como % no como tanto por uno(15 en lugar de 0.15)
# Asegurar que las cantidades en euros estén ajustadas al céntimo
# []

# Haz doble clic(o pulsa Intro) para editar

# []

# Retos
# Impedir que el usuario siga con el proceso si no introduce valores numéricos correctos
# Hacer una versión del programa que actúe al revés. Conociendo el tipo de interés, los años y periodos de imposición y sabiendo que suma total se quiere conseguir el programa debe indicar el capital inicial a invertir

# Toma de datos

cantidad_deseada = 0
while cantidad_deseada == 0:
    cantidad_deseada = input("Cantidad deseada: ")
    try:
        P = float(cantidad_deseada)
        if P <= 0:
            print("Debe introducir un número mayor que cero")
            cantidad_deseada = 0
    except:
        print("Debe introducir un número válido")
        cantidad_deseada = 0
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
n_veces = 0
while n_veces == 0:
    n_veces = input("Número de veces que se acumula el interés por año: ")
    try:
        n = int(n_veces)
        if n <= 0:
            print("Debe introducir un número de veces positivo y mayor que cero")
            n_veces = 0
    except:
        print("Debe introducir un valor válido.")
        n_veces = 0

# Cálculos

A = P / (1 + (r/n)) ** (n*t)

cantidad_a_invertir = A

# Muestra de resultados

print(f"Tras {anios} años de inversión al {interes} %, calculando cada {n_veces} el interés, para obtener {cantidad_deseada} su cantidad debe ser: {cantidad_a_invertir:.2f} €")
