#!/usr/bin/node
/*
Second class, Inhertance
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.s = size;
  }
}

module.exports = Square;
