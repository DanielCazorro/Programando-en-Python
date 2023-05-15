# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

def feet(length, width):
    area = length * width
    area_acre = area / 43560

    return area_acre

print(feet(50,50))