// # The program that you create for this exercise will begin by reading the cost of a meal ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip. Format the output so that all of the values
// # are displayed using two decimal places.

function tax_and_tip() {
    let cost_of_meal = parseFloat(prompt("Cost of a meal: "));
  
    let tax_cost = cost_of_meal * (21 / 100);
    let tip_cost = cost_of_meal * (18 / 100);
    let total = cost_of_meal + tax_cost + tip_cost;
  
    let cost_total = `Tax amount: ${tax_cost.toFixed(2)} €\nTip Amount: ${tip_cost.toFixed(2)} €\nGrand total: ${total.toFixed(2)} €`;
    console.log(cost_total);
  
    return cost_total;
  }
  
  tax_and_tip();
  