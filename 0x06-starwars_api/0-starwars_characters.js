#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    for (const character of res.characters) {
      request(character, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const res = JSON.parse(body);
          console.log(res.name);
        }
      });
    }
  }
});
