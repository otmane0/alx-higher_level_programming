#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args[0]);

if (isNaN(num) || num <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) { console.log('C is fun'); }
}
