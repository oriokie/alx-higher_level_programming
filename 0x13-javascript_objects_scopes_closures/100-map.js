#!/usr/bin/node
const list = require('./100-data').list;
let index = 0;
const map1 = list.map((x) => x * index++);
console.log(list);
console.log(map1);
