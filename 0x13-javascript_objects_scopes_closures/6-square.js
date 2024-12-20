#!/usr/bin/node
/*
Second class, Inhertance
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the parent class's constructor
  }

  charPrint(c) {
    if (c) {
      // Temporarily modify the parent's `print()` logic by overriding its behavior
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      // Use the parent class's `print()` method for default behavior
      super.print();
    }
  }
}

module.exports = Square;
