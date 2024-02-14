#!/usr/bin/node

const dict = require('./101-data').dict;

function occurrence (inputdict) {
  const occDict = {};
  for (const key in inputdict) {
    const occurances = inputdict[key];
    if (occurances in occDict) {
      occDict[occurances].push(key);
    } else {
      occDict[occurances] = [key];
    }
  }
  return (occDict);
}

const result = occurrence(dict);
console.log(result);
