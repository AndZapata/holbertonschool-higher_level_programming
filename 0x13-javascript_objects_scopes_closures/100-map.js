#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const map1 = list.map(function (num, index) {
  return num * index;
});
console.log(map1);
