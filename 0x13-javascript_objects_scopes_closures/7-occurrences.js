#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0; let i = 0;
  for (i; i < list.length; i++) {
    if (list[i] === searchElement) {
      n++;
    }
  }
  return n;
};
