#!/usr/bin/node
const dict = require('./101-data').dict;

const listOfKey = [];
const dictOfVal = {};
for (const key in dict) {
  listOfKey.push(key);
  dictOfVal[dict[key]] = [];
}

for (const val of listOfKey) {
  for (const keys in dictOfVal) {
    if (dict[val].toString() === keys) {
      dictOfVal[keys].push(val);
    }
  }
}

console.log(dictOfVal);
