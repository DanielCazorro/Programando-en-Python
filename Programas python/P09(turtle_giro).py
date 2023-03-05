# Añadimos un giro en el bucle for, así vemos como se puden dibujar formas y la potencia del bucle
import turtle

miTortuga = turtle.Turtle()

strLados = input("¿Cuántos lados quieres? ")
lados = int(strLados)
strTam = input("¿De que tamaño los quieres? ")
Tam = int(strTam)

for _ in range(0, 360, 15):
    for _ in range(0, lados):
        miTortuga.forward(Tam)
        miTortuga.left(360/lados)
    miTortuga.left(15)
