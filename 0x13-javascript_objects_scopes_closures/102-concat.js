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

// read from first source file
fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  // read from second source file
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    // data to write into destination file
    const content = `${dataA}${dataB}`;
    // writing into destination file
    fs.writeFile(fileC, content, err => {
      if (err) {
        console.error(err);
      }
    });
  });
});
