#!/usr/bin/node
const arg = process.argv[2];
const x = (isNaN(arg) ? 'Missing number of occurrences' : arg);
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}
