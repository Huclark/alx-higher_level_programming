#!/usr/bin/node
/**
 * This script prints the number of movies where the character "Wedge Antilles" is
 * present
 */
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);
    let count = 0;

    // Loop through each film and check if Wedge Antilles is present
    filmsData.results.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});
