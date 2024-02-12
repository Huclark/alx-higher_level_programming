#!/usr/bin/node
/**
 * This script searches for the second biggest integer in the list of arguments
 * It prints 0 if zero or one argument is passed
 */
const argvLength = process.argv.length;
if (argvLength <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2, argvLength);
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
