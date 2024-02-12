#!/usr/bin/node
// script that prints the addition of 2 integers

function add (a, b) {
  const sum = a + b;
  return (sum);
}
const myNum1 = parseInt(process.argv[2]);
const myNum2 = parseInt(process.argv[3]);

console.log(add(myNum1, myNum2));
