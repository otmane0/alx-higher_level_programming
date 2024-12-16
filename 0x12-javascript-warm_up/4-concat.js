#!/usr/bin/node

const args = process.argv.slice(2);
let secondArg = args[1];
if (secondArg === undefined) {
  secondArg = 'undefined';
}

console.log(args[0] + ' is ' + secondArg);
