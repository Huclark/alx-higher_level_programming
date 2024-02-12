#!/usr/bin/node

/**
 * This script prints a square with the 'X' character
 * where the first argument is the size of the square
 */
const size = parseInt(process.argv[2]);
let height = 0;

if (size) {
  while (height < size) {
    console.log('X'.repeat(size));
    height++;
  }
} else {
  console.log('Missing number of occurrences');
}
