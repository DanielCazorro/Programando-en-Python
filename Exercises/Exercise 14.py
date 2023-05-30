# Exercise 14: Height Units

# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.

def heightUnits(feet, inches):
    """
    Convierte feet and inches en cm
    """
    totalCM = 0

    inches += feet *12
    totalCM = inches * 2.54

    print(totalCM)
    return totalCM

# heightUnits(1,12)

## CONSOLE version
# Convert a height in feet and inches to centimeters.
#
IN_PER_FT = 12
CM_PER_IN = 2.54
# Read the height from the user
print("Enter your height:")
feet = int(input(" Number of feet: "))
inches = int(input(" Number of inches: "))
# Compute the equivalent number of centimeters
cm = (feet * IN_PER_FT + inches) * CM_PER_IN
# Display the result
print("Your height in centimeters is:", cm)