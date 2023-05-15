// # In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a
// # $0.25 deposit.
// # Write a program that reads the number of containers of each size from the user.
// # Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and two digits to the right of the decimal point.

function recycle() {
    let less_one = parseInt(prompt("Number of containers one liter or less: "));
    let more_one = parseInt(prompt("Number of containers more than one liter: "));
  
    let less_total = less_one * 0.10;
    let more_total = more_one * 0.25;
  
    let total = less_total + more_total;
  
    console.log(`The total amount that you'll receive is: ${total.toFixed(2)} $`);
  }
  
  recycle();
  