#!/usr/bin/node

const request = require('request');

const url = process.argv[2].toString();

request.get(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const char of film.characters) {
      if (char.endsWith('18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
