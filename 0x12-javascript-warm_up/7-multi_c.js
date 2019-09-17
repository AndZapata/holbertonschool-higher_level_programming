#!/usr/bin/node
if (Number.isInteger(parseInt(process.argv[2]))) {
  for (let c = 0; c < parseInt(process.argv[2]); c++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
