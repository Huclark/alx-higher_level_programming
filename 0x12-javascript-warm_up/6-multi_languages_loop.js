#!/usr/bin/node

/**
 * prints 3 lines by using an array of string and a loop
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
