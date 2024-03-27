#!/usr/bin/node
/**
 * This script displays the status code of a GET request
 */
const request = require('request');

// Send a GET request to the provided URL
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
