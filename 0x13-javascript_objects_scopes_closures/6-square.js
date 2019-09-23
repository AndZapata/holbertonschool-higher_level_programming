#!/usr/bin/node
const Rec = require('./4-rectangle');

class Square extends Rec {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
