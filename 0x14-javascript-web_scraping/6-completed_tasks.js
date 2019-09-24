#!/usr/bin/node
/* Import module fs to open and write a file */
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const list = JSON.parse(body);
    for (const i of list) {
      if (i.completed === true) {
        if (dict[i.userId] === undefined) dict[i.userId] = 1;
        else dict[i.userId]++;
      }
    }
    console.log(dict);
  }
});
