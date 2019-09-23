#!/usr/bin/node
const Squ = require('./5-square');

class Square extends Squ {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
