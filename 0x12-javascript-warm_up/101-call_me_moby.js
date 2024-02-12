#!/usr/bin/node
/**
 * This function executes x times a function
 */
exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
