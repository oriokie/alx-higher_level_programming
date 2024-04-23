#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const characterId = '18';
    let count = 0;
    for (const film of films) {
      if (film.characters.some(characterUrl => characterUrl.includes(`/${characterId}/`))) {
        count++;
      }
    }
    console.log(count);
  }
});
