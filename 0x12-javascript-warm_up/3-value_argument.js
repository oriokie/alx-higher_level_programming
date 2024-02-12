#!/usr/bin/node
// SCript that prints the first arg

const firstArg = process.argv[2];

if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
