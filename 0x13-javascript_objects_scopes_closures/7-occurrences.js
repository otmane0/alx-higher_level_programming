#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (let i = 0; i < list.lenght; i++) {
    if (list[i] === searchElement) {
      n += 1;
    }
  }
  return n;
};
