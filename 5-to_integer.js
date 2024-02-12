#!/usr/bin/node
// script that prints numbers first arg

const input = parseInt(process.argv[2]);

if (!isNaN(input)) {
  console.log(`My number: ${input}`);
} else {
  console.log('Not a number');
}
