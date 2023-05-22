# Exercise 10: Arithmetic
# (Solved, 22 Lines)
# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.
from math import log10


def arithmetic(a, b):
    """
    Lee dos números enteros y devuelve varias operaciones de los mismos
    """

    sum_numbers = a + b
    difference_numbers = a - b
    product_numbers = a * b
    quotient_numbers = a / b
    remainder_numbers = a % b
    log_numbers = log10(a)
    elevate_numbers = a**b

    result = f"The sum of a and b: {sum_numbers}\nThe difference when b is subtracted from a: {difference_numbers}\n The product of a and b: {product_numbers}\nThe quotient when a is divided by b: {quotient_numbers}\nThe remainder when a is divided by b: {remainder_numbers}\nThe result of log10 a: {log_numbers}\nThe result of ab: {elevate_numbers}"
    
    return result

print(arithmetic(1,2))