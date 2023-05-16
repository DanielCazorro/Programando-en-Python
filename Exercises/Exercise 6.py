# The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

def tax_and_tip():
    """
    
    """
    cost_of_meal = float(input("Cost of a meal: "))

    tax_cost = cost_of_meal * (21/100)
    tip_cost = cost_of_meal * (18/100)
    total = cost_of_meal + tax_cost + tip_cost

    cost_total = print(f"Tax amount: {tax_cost} €\nTip Amount: {tip_cost}\nGrand total: {total} €")

    return cost_total

tax_and_tip()