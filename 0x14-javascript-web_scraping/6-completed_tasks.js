#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const tasks = JSON.parse(body);
  const result = {};
  for (const task of tasks) {
    if (task.completed === true) {
      if (task.userId in result) {
        result[task.userId] += 1;
      } else {
        result[task.userId] = 1;
      }
    }
  }
  console.log(result);
});
