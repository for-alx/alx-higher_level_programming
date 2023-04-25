#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2].toString();
const fileName = process.argv[3].toString();

request.get(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(fileName, body, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
