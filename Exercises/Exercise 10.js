// # Exercise 10: Arithmetic
// # (Solved, 22 Lines)
// # Create a program that reads two integers, a and b, from the user.Your program should
// # compute and display:
// # • The sum of a and b
// # • The difference when b is subtracted from a
// # • The product of a and b
// # • The quotient when a is divided by b
// # • The remainder when a is divided by b
// # • The result of log10 a
// # • The result of ab
// # Hint: You will probably find the log10 function in the math module helpful
// # for computing the second last item in the list.

function arithmetic(a, b) {
    /*
    Reads two integers and returns various operations on them
    */
    const log10 = Math.log10;
  
    let sum_numbers = a + b;
    let difference_numbers = a - b;
    let product_numbers = a * b;
    let quotient_numbers = a / b;
    let remainder_numbers = a % b;
    let log_numbers = log10(a);
    let elevate_numbers = Math.pow(a, b);
  
    let result = `The sum of a and b: ${sum_numbers}\nThe difference when b is subtracted from a: ${difference_numbers}\nThe product of a and b: ${product_numbers}\nThe quotient when a is divided by b: ${quotient_numbers}\nThe remainder when a is divided by b: ${remainder_numbers}\nThe result of log10 a: ${log_numbers}\nThe result of ab: ${elevate_numbers}`;
  
    return result;
  }
  
  console.log(arithmetic(1, 2));
  