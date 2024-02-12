#!/usr/bin/node
/**
 * This script computes and prints a factorial
 * The first argument is an integer used for computing the factorial
 */
function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
