#!/usr/bin/node
const s = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < s; i++) {
    console.log('X'.repeat(s));
  }
}
