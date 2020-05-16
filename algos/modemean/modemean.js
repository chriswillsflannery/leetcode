// Given an array of numbers, determine if the mode and mean of the array are equivalent

//  Caveats:
//  Math.floor the mean
//  If there are multiple modes, use the max of the modes
//  Return true or false

function getMean(arr) {
  // get sum of all elements in array
  const sum = arr.reduce((a, b) => a + b);
  // const sum = arr.reduce((acc, curr) => {
  //   acc += curr;
  //   return acc;
  // }, 0);
  // divide that sum by arr.length
  const divided = sum / arr.length;
  // floor it and return 
  return Math.floor(divided);
}

function getMode(arr) {
  // create a cache of numbers and their # of instances
  const cache = {};
  arr.forEach(num => {
    cache[num] ? cache[num] += 1 : cache[num] = 1;
  })
  // console.log('cache', cache);

  // store current greatest mode we've seen so far and its corresponding # of occurences
  let maxKey = 0;
  let maxVal = 0;
  // looping over cache
  for (let key in cache) {
    let val = cache[key];
    // check if any given val we've seen so far is greater than current maxVal and current Number(key) is greater than current maxKey, set maxKey to current Number(key) and maxVal to current val
    if (val >= maxVal && Number(key) > maxKey) {
      maxKey = Number(key);
      maxVal = val;
    }
  }

  // return maxKey
  return maxKey;
}

function modeMean(arr) {
  return getMean(arr) === getMode(arr);
}

// console.log(modeMean([1, 2, 2, 3, 3, 4, 5])); // mode 3. mean 2. false
// console.log(modeMean([1, 2, 2, 3, 3, 4, 6])); // mode 3. mean 3. true
// console.log(modeMean([6, 4, 3, 3, 2, 2, 1])); // true
