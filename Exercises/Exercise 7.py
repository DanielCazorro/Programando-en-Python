# Exercise 7: Sum of the First n Positive Integers
# (Solved, 11 Lines) Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1) 2

def sumAll(number):
    """
    Recibe un número y devuelve la suma de todos los entereros hasta el mismo
    """
    sum = ((number)*(number + 1)) / 2

    return sum

print(sumAll(4))