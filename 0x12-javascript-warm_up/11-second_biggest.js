#!/usr/bin/node
/**
 * This script searches for the second biggest integer in the list of arguments
 * It prints 0 if zero or one argument is passed
 */
const argvLength = process.argv.length;
if (argvLength <= 3) {
  console.log(0);
} else {
  let biggestNumber = parseInt(process.argv[2]);
  let secondBiggest = biggestNumber;
  let currentNumber;
  let index = 2;

  while (index < argvLength) {
    currentNumber = parseInt(process.argv[index]);
    if (biggestNumber < currentNumber) {
      secondBiggest = biggestNumber;
      biggestNumber = currentNumber;
    }
    if (currentNumber > secondBiggest && currentNumber < biggestNumber) {
      secondBiggest = currentNumber;
    }
    index++;
  }
  console.log(secondBiggest);
}
