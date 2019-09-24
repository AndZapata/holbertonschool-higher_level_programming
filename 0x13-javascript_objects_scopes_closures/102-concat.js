#!/usr/bin/node
const file = require('fs');
let description;
description = file.readFileSync(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  return data;
});

file.appendFile(process.argv[4], description, function (err, data) {
  if (err) {
    console.log(err);
  }
});

description = file.readFileSync(process.argv[3], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
  return data;
});

file.appendFile(process.argv[4], description, function (err, data) {
  if (err) {
    console.log(err);
  }
});
