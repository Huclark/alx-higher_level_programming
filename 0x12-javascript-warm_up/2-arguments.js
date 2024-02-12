#!/usr/bin/node

/**
 * This script prints a message depending on the number of arguments
 * passed.
 * If no arguments are passed to the script, it prints "No argument"
 * If only one argument is passed to the script, it prints "Argument found"
 * Otherwise it prints "Arguments found"
 */
process.argv.length < 3
  ? console.log('No argument')
  : process.argv.length === 3
    ? console.log('Argument found')
    : console.log('Arguments found');
