# Creamos una variable que se llame lados, para poder añadir mas bucles if si son necesarios
import turtle

miTortuga = turtle.Turtle()

strLados = input("¿Cuántos lados quieres? ")
lados = int(strLados)

if lados == 3:

    for _ in range(0, lados):
        miTortuga.forward(100)  # Aquí avanzamos 100 pixels
        miTortuga.left(120)  # Aquí giramos 120 grados

elif lados == 4:
    for _ in range(0, lados):
        miTortuga.forward(100)  # Aquí avanzamos 100 pixels
        miTortuga.left(90)  # Aquí giramos 90 grados

else:
    print("No se dibujar más que cuadrados y triángulos")
