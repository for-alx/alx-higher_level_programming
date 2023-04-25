#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  console.log(JSON.parse(body).title);
});
