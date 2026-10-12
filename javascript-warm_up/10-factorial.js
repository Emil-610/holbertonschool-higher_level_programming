#!/usr/bin/node
// Computes and prints the factorial of the integer given as first argument
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(n));
