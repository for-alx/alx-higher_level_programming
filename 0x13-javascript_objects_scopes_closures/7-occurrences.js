#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let found = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      found += 1;
    }
  }
  return found;
};
