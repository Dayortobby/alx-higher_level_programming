#!/usr/bin/node

// a script checking if argument was passed to it
if (process.argv[2] === undefined ) {
  console.log("No argument")
} else {
  console.log(process.argv[2])
}
