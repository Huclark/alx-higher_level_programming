#!/usr/bin/node

/**
 * This script prints x times "C is fun"
 * where x is the number of times the string
 * will be printed and x is the first argument of the script
 */
const x = parseInt(process.argv[2]);
let index = 0;

if (x) {
  while (index < x) {
    console.log('C is fun');
    index++;
  }
} else {
  console.log('Missing number of occurrences');
}
