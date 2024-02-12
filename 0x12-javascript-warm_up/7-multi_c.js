#!/usr/bin/node
// scripting for printing 'C is fun' x times

const times = parseInt(process.argv[2]);

if (!isNaN(times)) {
  let count = 0;
  while (count < times) {
    console.log('C is fun');
    count++;
  }
} else {
  console.log('Missing number of occurrences');
}
