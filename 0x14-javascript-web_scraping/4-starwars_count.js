#!/usr/bin/node

const request = require('request');

// const url = process.argv[2].toString();

const url2 = 'https://swapi-api.alx-tools.com/api/people/18';

request.get(url2, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body).films.length);
});
