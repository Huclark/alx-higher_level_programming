#!/usr/bin/node
/**
 * This script prints 3 lines:
 * The first line: "C is fun"
 * The second line: "Python is cool"
 * The third line: "JavaScript is amazing"
 */
let index = 0;
const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

while (index < lines.length) {
  console.log(lines[index]);
  index++;
}
