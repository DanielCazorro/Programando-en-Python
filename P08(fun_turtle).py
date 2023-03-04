# Realizamos operación para que en función de los lados pueda crear el programa la figura deseada
import turtle

miTortuga = turtle.Turtle()

strLados = input("¿Cuántos lados quieres? ")
lados = int(strLados)
strTam = input("¿De que tamaño los quieres? ")
Tam = int(strTam)

for _ in range(0, lados):
    miTortuga.forward(Tam)
    miTortuga.left(360/lados)
