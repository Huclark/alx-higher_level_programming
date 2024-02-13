#!/usr/bin/node
/**
 * This function returns the reversed version of a list
 */
exports.esrever = (list) => {
  const new_list = [];
  const len = list.length;
  for (let i = len - 1; i >= 0; i--) {
    new_list.push(list[i]);
  }
  return new_list;
};
