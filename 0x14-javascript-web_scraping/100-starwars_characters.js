#!/usr/bin/node

/**
 * script that prints all characters of a Star Wars movie
 */

if (process.argv.length > 2) {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
  const request = require('request');

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const jsonData = JSON.parse(body);

    jsonData.characters.forEach(element => {
      request(element, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        const charData = JSON.parse(body);
        console.log(charData.name);
      });
    });
  });
}
