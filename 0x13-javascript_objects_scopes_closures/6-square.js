#!/usr/bin/node

/*
Square Class
 */
const dadSquare = require('./5-square');

class Square extends dadSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i; let j; const tre = '';
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
