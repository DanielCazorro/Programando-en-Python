# In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and two digits to the right of the decimal point.

def recycle():
    less_one = int(input("Number of continers one liter or less: "))
    more_one= int(input("Number of containers more than one liter: "))

    less_total = less_one * 0.10
    more_total = more_one * 0.25

    total = less_total + more_total

    print(f"The total amount that you'll receive is: {total:.2f} $")

recycle()
