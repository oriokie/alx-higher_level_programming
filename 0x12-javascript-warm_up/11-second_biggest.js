#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

const len = args.length;

if (len <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  const secondB = args[1];
  console.log(secondB);
}
