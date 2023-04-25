#!/usr/bin/node

const request = require('request');

const url = process.argv[2].toString();
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  let film = '';
  for (film of films) {
    if (film.characters.includes(actor)) {
      count += 1;
    }
  }
  console.log(count);
});
