#!/usr/bin/node
/**
 * This function increments and calls a function
 */
exports.addMeMaybe = function (number, theFunction) {
  ++number;
  theFunction(number);
};
