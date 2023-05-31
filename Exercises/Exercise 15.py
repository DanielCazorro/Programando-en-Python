# Exercise 15: Distance Units

# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

def distanceUnits(feet):
    """
    Convierte y muestra feet en inches, yards y miles
    """
    inches = feet * 12
    yards = feet * 0.333333
    miles = feet * 0.000189394

    print(f"Feet: {feet}\n----------\nYards: {yards}\nInches: {inches}\nMiles: {miles}")

distanceUnits(50)