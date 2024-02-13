#!/usr/bin/node
/**
 * This function returns the number of occurences in a list
 */
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
