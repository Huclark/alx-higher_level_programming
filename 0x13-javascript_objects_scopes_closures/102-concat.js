#!/usr/bin/node
/**
 * This script concatenates 2 files
 * Syntax: ./102-concat.js <fileA> <fileB> <fileC>
 * where the;
 * first argument is the file path of the first source file
 * second argument is the file path of the second source file
 * third argument is the file path of the destination
 */
const fs = require('fs');
const [fileA, fileB, fileC] = process.argv.slice(2);

try {
  // read from first source file synchronously
  const dataA = fs.readFileSync(fileA, 'utf8');
  // read from second source file synchronously
  const dataB = fs.readFileSync(fileB, 'utf8');
  // write into destination file synchronously
  fs.writeFileSync(fileC, dataA + dataB);
} catch (err) {
  console.error(err);
}
