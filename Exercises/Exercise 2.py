# Exercise 2: Hello
# Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.

def hello():
    """
    Programa que te pide tu nombre y te contesta con un saludo
    """
    name = input("Escriba su nombre: ")
    print(f"Hola {name}! Es un placer estar aquí con usted")

hello()