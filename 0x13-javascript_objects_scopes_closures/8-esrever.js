#!/usr/bin/node

exports.esrever = function (list) {
  const new_list = [];
  for (let i = list.length - 1, n = 0; i >= 0; i--, n++) {
    new_list[n] = list[i];
  }
  return new_list;
};
