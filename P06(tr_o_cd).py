# Realizamos cuadrado o triángulo utilizando variables
import turtle

miTortuga = turtle.Turtle()

respuesta = input("¿Quieres un triángulo?(S/N) ")

if respuesta == 'S' or respuesta == 's':

    for _ in range(0, 3):
        miTortuga.forward(50)  # Aquí avanzamos 50 pixels
        miTortuga.left(120)  # Aquí giramos 120 grados

else:
    for _ in range(0, 4):
        miTortuga.forward(50)  # Aquí avanzamos 50 pixels
        miTortuga.left(90)  # Aquí giramos 90 grados
