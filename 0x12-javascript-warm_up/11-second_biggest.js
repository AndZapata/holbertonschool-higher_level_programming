#!/usr/bin/node
const uList = process.argv;
if (uList.length <= 3) {
  console.log(0);
} else {
  console.log(uList.sort((a, b) => a - b).slice(-2)[0]);
}
