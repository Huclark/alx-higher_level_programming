#!/usr/bin/node

/**
 * script that gets the contents of a webpage and stores it in a file.
 */

if (process.argv.length > 3) {
  const url = process.argv[2];
  const filePath = process.argv[3];
  const request = require('request');
  const fs = require('fs');

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error reading file:', err);
      }
    });
  });
}
