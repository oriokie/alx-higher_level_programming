#!/usr/bin/node

exports.logMe = function (item) {
  let count = 0;

  return function (item) {
    count++;
    console.log(`${count}: ${item}`);
  };
};
