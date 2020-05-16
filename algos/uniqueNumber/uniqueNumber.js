/**
 * Write a function that will take an array of integers, all of which will appear exactly twice,
 * except for one integer that will appear exactly once. Return the integer that appears once.
 *
 * uniqueNumber([1,2,1,3,3]); -> 2 sum: 10
 *
 * BONUS:
 * Complete the challenge in O(n) time
 * Complete the challenge in O(1) space
 *
 */

//cache
function uniqueNumberCache(arr) {
  const cache = Object.create(null);
  arr.forEach(el => {
    cache[el] ? cache[el] += 1 : cache[el] = 1;
  });
  for (let key in cache) {
    if (cache[key] === 1) return key;
  }
  return -1;
};

// console.log(uniqueNumberCache([1, 2, 3, 1, 3]));

//no extra memory used
function uniqueNumberNoX(arr) {
  const copy = arr.slice().sort();
  for (let i = 0; i < copy.length; i++) {
    let prev = arr[i - 1];
    let curr = arr[i];
    let next = arr[i + 1];
    if (prev !== curr && next !== curr) return curr;
  }
  return -1;
}

console.log(uniqueNumberNoX([1, 2, 3, 2, 3]));