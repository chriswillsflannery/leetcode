/***************************************************************************

Target Sum for Array of Integers

1. Write a function that receives two parameters; a non-empty array of distinct integers and an integer representing a target sum

2. If any two numbers in the input array sum up to equal the target sum value, then return the two values within an array

3. If no two numbers sum up to the target sum, then return an empty array

4. You can assume that there will be at most one pair of numbers that when summed will equal the target sum

Sample Input: [2,3,4,5,9,7,-5,8,-2,-1], 1
Sample Result: [2,-1]

Considerations
1. Be mindful of performance
2. There is a possibility large arrays may be passed to this function

***************************************************************************/

// Sample Inputs

const test1 = [[3, 5, -4, 8, 11, 1, -1, 6], 10]; // => [-1,11]
const test2 = [[-1, 1, 2, 3, 6, 7], 10];
// const test = [[1,2,3,4,5,6,7,8,9], 17] // => [8,9]
// const test = [[1,2,3,4,5,6,7,8,9,15], 18] // => [3,15]
// const test = [[-7,-5,-3,-1,0,1,3,5,7], -5] // => [-5,0]
// const test = [[-21,301,12,4,65,56,210,356,9,-47], 164] // => []

// Start Code Here

function targetSum(ints, target) {
  const complements = {};
  for (let i = 0; i < ints.length; i++) {
    const int = ints[i];
    const complement = target - int;
    if (complements[int]) return [int, complement];
    complements[complement] = true;
  }
  return false;
}

// console.time();
// console.log(targetSum(test[0], test[1]));
// console.timeEnd();
