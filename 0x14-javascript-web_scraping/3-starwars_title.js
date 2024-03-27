#!/usr/bin/node
/**
 * This script prints the title of a Star Wars movie where the episode
 * number matches a given integer
 */
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
