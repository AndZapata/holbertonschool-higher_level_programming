#!/usr/bin/node
/* Import module fs to open and write a file */
const request = require('request');
const file = require('fs');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    file.writeFile(process.argv[3], body, 'utf-8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
