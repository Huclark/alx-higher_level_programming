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

  // This prints the rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // This exchanges width and height values with each other
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // This multiplies the width and height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
