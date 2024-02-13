#!/usr/bin/node
/**
 * This script imports a dictionary of occurences by user id and
 * computes a dictionary of user ids by occurence and
 * prints the new dictionary
 * In the new dictionary:
 * a key is a number of occurences
 * a value is the list of user ids
 */
// Import the dictionary
const { dict } = require('./101-data');
const newDict = {};
for (const [occurences, userId] of Object.entries(dict)) {
  if (!newDict[userId]) {
    newDict[userId] = [];
  }
  newDict[userId].push(occurences);
}
console.log(newDict);
