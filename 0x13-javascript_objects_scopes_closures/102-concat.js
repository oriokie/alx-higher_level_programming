#!/usr/bin/node

const fileSystem = require('fs');

const fileA = fileSystem.readFileSync(process.argv[2], 'utf-8');
const fileB = fileSystem.readFileSync(process.argv[3], 'utf-8');
fileSystem.writeFileSync(process.argv[4], fileA + fileB, 'utf-8');
