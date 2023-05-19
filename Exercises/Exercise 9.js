// # Exercise 9: Compound Interest
// # (19 Lines) Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each
// # amount so that it is rounded to 2 decimal places.

function compoundInterest(initial_amount = 0, years = 1) {
    /*
    Compound interest program
    */
    let money = initial_amount;
    // Earn 4 percent interest each year and add it to the account for the next year
    for (let i = 0; i < years; i++) {
      let percent = money * 0.04;
      money += percent;
    }
  
    return Math.round(money * 100) / 100;
  }
  
  console.log(compoundInterest(100, 5));
  
