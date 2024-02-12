#!/usr/bin/node

/**
 * This script prints "My number: <first argument converted in integer>"
 * If the first argument can be converted to an integer.
 * If the argument can’t be converted to an integer, it prints “Not a number”
 */
const num = parseInt(process.argv[2]);

num
  ? console.log(`My number: ${num}`)
  : console.log('Not a number');
