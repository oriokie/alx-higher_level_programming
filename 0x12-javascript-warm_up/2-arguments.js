#!/usr/bin/node
// script that print a message depending on the number of args passed

const args = process.argv.length;

if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
