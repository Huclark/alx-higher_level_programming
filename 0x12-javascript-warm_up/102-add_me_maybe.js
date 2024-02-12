#!/usr/bin/node
/**
 * This function increments and calls a function
 */
exports.addMeMaybe = function (number, theFunction) {
  const newNumber = number + 1;
  theFunction(newNumber);
};
