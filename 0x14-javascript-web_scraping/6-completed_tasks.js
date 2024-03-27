#!/usr/bin/node

/**
 * script that computes the number of tasks completed by user id.
 */

if (process.argv.length > 2) {
  const url = process.argv[2];
  const request = require('request');

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const data = JSON.parse(body);
    const mydict = {};

    data.forEach(item => {
      if (item.completed === true) {
        const id = item.userId;
        mydict[id] = (mydict[id] || 0) + 1;
      }
    });

    console.log(mydict);
  });
}
