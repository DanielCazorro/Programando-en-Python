# Relizamos ejercicios básicos con turtle utilizando un bucle for
import turtle

miTortuga = turtle.Turtle()

for _ in range(0, 4):
    miTortuga.forward(50)  # Aquí avanzamos 50 pixels
    miTortuga.left(90)  # Aquí giramos 90 grados
