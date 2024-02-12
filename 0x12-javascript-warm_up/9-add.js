#!/usr/bin/node
/**
 * This script prints the addition of 2 integers
 * Where the first argument is the first integer and
 * the second argument is the second integer
 */
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
