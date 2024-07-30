#!/usr/bin/node

const fs = require('fs');

// Check if the file path is provided
if (process.argv.length < 3) {
  console.error('Usage: ./readFile.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
