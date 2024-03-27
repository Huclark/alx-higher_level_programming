#!/usr/bin/node
/**
 * This script reads and prints the content of a file
 * The first argument is the file path 
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */
const fs = require('fs')

// Check if the file path is provided as an argument
if (!process.argv[2]) {
    console.error('Usage: ./0-readme.js <path to file>')
    process.exit(1)
}

// Read the file contenct
fs.readFile(process.argv[2], 'utf-8', (error, data) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
