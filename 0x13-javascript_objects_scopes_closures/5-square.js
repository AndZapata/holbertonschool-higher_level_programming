#!/usr/bin/node
const Rec = require('./4-rectangle');

class Square extends Rec {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
