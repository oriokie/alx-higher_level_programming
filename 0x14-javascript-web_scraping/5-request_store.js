#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const filePath = process.argv[3];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8');
  }
});
