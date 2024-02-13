#!/usr/bin/node
/**
 * This script defines a square and inherits from the Rectangle
 * class of 4-rectangle.js file
 * Constructor takes only one argument: size
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
