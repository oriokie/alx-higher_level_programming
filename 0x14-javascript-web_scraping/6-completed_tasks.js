#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);

    tasks.forEach(task => {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    });

    console.log(completed);
  }
});
