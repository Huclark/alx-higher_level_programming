#!/usr/bin/node
/**
 * This script defines a Rectangle class
 * With the constructor taking two arguments:
 * w: width of rectangle
 * h: height of rectangle
 */
class Rectangle {
  width;
  height;
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
