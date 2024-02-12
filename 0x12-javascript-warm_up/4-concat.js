#!/usr/bin/node
// script for printing two arguments add is cool

const firstArg = process.argv[2];
const secondArg = process.argv[3];
if (firstArg && secondArg) {
  console.log(firstArg, 'is', secondArg);
} else if (firstArg) {
  console.log(firstArg, 'is undefined');
} else {
  console.log('undefined is undefined');
}
