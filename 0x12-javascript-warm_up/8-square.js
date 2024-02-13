#!/usr/bin/node

/**
 * This script prints a square with the 'X' character
 * where the first argument is the size of the square
 */
const process = require('process');
const firstArg = process.argv[2];
const size = parseInt(firstArg);

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
} else {
  console.log('Missing size');
}
