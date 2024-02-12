#!/usr/bin/node

/**
 * This script prints the first argument passed to it:
 * If there are no arguments, it prints 'No argument'
 */
!process.argv[2]
  ? console.log('No argument')
  : process.argv.slice(2).forEach((argument) => {
    console.log(argument);
  });
