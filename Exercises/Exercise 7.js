// # Exercise 7: Sum of the First n Positive Integers
// # (Solved, 11 Lines) Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be
// # computed using the formula:
// # sum = (n)(n + 1) 2

function sumAll(number) {
    /*
    Receives a number and returns the sum of all integers up to that number
    */
    let sum = (number * (number + 1)) / 2;
  
    return sum;
  }
  
  console.log(sumAll(4));
  