# Exercise 3: Area of a Room
# Write a program that asks the user to enter the width and length of a room. Once these values have been read, your program should compute and display the area of the room. The length and the width will be entered as floating-point numbers. Include units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

def area_of_a_room():
    """
    Pide tamaño de habitación y da el área
    """
    width = float(input("Ancho: "))
    lenght = float(input("Alto: "))

    area = width * lenght

    print(f"Su habitación de {width:.2f} metros de ancho y {lenght:.2f} metros de alto tiene un área de: {area:.2f} metros cuadrados")

area_of_a_room()