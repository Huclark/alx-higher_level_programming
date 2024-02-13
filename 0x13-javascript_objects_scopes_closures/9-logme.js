#!/usr/bin/node
/**
 * This function prints the number of arguments already
 * printed and the new argument value.
 * Output Format: <number arguments already printed>: <current argument value>
 */
let logCount = 0;
exports.logMe = (item) => {
  console.log(`${logCount}: ${item}`);
  logCount++;
};
