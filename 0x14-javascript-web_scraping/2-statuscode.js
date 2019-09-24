#!/usr/bin/node
/* Import module fs to open and write a file */
const request = require('request');
const url = process.argv[2];
request (url, function (error, response, body) {
 if (err) {
  console.log(error);
 } else {
  console.log(JSON.parse(body).name);
 }
});
