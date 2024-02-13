#!/usr/bin/node
/**
 * This script defines a Rectangle class which prints a rectangle.
 * The constructor takes 2 arguments:
 * w: width of rectangle
 * h: height of rectangle
 * If w or h is 0 or not a positive integer,
 * an empty object is created
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
