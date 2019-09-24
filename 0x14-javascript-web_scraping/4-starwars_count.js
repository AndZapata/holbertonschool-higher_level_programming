#!/usr/bin/node
/* Import module fs to open and write a file */
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    let list = [];
    const BigList = JSON.parse(body).results;
    for (const i of BigList) {
      list = i.characters;
      for (const j of list) {
        if (j.includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
