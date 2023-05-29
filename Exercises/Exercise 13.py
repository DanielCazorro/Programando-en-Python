# Exercise 13: Making Change

# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.
# A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
# because one side of the coin has a loon (a type of bird) on it. The two dollar
# coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
# from the combination of the number two and the name of the loonie.

##
# Compute the minimum collection of coins needed to represent a number of cents.
#
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5
# Read the number of cents from the user
cents = int(input("Enter the number of cents: "))
# Determine the number of toonies by performing an integer division by 200. Then compute
# the amount of change that still needs to be considered by computing the remainder after
# dividing by 200.
print(" ", cents // CENTS_PER_TOONIE, "toonies")
cents = cents % CENTS_PER_TOONIE

# Repeat the process for loonies, quarters, dimes, and nickels
print(" ", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE
print(" ", cents // CENTS_PER_QUARTER, "quarters")
cents = cents % CENTS_PER_QUARTER
print(" ", cents // CENTS_PER_DIME, "dimes")
cents = cents % CENTS_PER_DIME
print(" ", cents // CENTS_PER_NICKEL, "nickels")
cents = cents % CENTS_PER_NICKEL
# Display the number of pennies
print(" ", cents, "pennies")