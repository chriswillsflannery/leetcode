/*
Given a multidimensional array with depth of n,
flatten it. Once flattened make it available as a
method on array instance
*/

const arr = [1, [2,3], 4, [5,[6,7]]];

const flatten = (arr) => {
  const newArr = [];
  arr.forEach(el => {
    if (typeof el === 'number') {
      newArr.push(el);
    } else if (typeof el === 'object') {
      newArr.push(...flatten(el));
    }
  });
  return newArr;
};

// console.log(flatten(arr));

Array.prototype.flatten = function() {
  return flatten(this);
};

console.log(arr.flatten());
