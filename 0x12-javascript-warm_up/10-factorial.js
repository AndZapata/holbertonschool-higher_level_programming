#!/usr/bin/node
const a = parseInt(process.argv[2]);
const fact = function (n) {
  if (n === 0 || !n) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
};

console.log(fact(a));
