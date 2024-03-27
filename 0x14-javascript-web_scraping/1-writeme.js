#!/usr/bin/node
/**
 * This script writes a string into a file
 */
const fs = require('fs');

// Write content to the file
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
