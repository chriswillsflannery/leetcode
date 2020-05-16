// Create a function called addingToX that accepts a number as an argument.

// It will return the sum of every integer from 1 up to and including the input number.

// addingToX(0) will return 0
// addingToX(1) will return 1
// addingToX(2) will return 3
// addingToX(3) will return 6
// addingToX(4) will return 10
// addingToX(5) will return 15
// addingToX(10) will return 55

function addingToX(num) {
  if (typeof num !== 'number') throw new TypeError('wrong input type');
  // keep sum variable
  let sum = 0;
  // loop upwards to num including num
  for (let i = 0; i <= num; i++) {
    // add current num to sum
    sum += i;
  }
  // return sum
  return sum;
}

// console.log(addingToX('chris')); 

// Challenge Part 2
// Write a function arrayToX that accepts a number as an argument.

// It will return an array where each element is the return value of calling addingToX on each integer from 1 up to and including the input number.

// arrayToX(1) will return [1]
// arrayToX(2) will return [1, 3]
// arrayToX(3) will return [1, 3, 6]
// arrayToX(4) will return [1, 3, 6, 10]
// arrayToX(5) will return [1, 3, 6, 10, 15]

function arrayToX(num) {
  // instantiate new array []
  const newArray = [];
  // loop up to and including num
  for (let i = 1; i <= num; i++) {
    // on each iteration, call addingtoX and push return value into new array
    newArray.push(addingToX(i));
  }
  // return new array;
  return newArray;
}

// console.log(arrayToX(5));