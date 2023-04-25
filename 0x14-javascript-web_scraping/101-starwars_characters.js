#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function helpRequest (actors, index) {
  if (index === actors.length) {
    return;
  }
  request(actors[index], function (error, response, body) {
    if (error) { console.log(error); }
    console.log(JSON.parse(body).name);
    helpRequest(actors, index + 1);
  });
}
request(url, function (error, response, body) {
  if (error) { console.error(error); }
  const result = JSON.parse(body).characters;
  helpRequest(result, 0);
});
