#!/usr/bin/node
/**
 * This script imports an array and computes a new array.
 */
const list = require('./100-main').list;
console.log(list);
const newList = list.map((number, index) => number * index;);
console.log(newList);
