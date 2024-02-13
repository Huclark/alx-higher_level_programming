#!/usr/bin/node
/**
 * This script defines a Square class
 * and inherits from the Square class of 5-square.js file
 * Constructor takes only one argument: size
 */
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  // This prints the square
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
