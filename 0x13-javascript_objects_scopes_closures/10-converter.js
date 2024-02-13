#!/usr/bin/node
/**
 * This function converts a number from base 10 to
 * another base passed as an argument
 * @param {number} base - The base to convert to.
 * @returns {function} - A converter function
 */
exports.converter = (base) => {
  return (decimalNumber) => {
    return decimalNumber.toString(base);
  };
};
