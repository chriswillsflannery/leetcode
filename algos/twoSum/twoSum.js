/*

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/

const expectEquals = require('../../utils/assertionTests');

function twoSum(nums, target) {
  const oppos = {}; // { 7:0, }
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (oppos[num] !== undefined) {
      return [oppos[num], i];
    } else {
      oppos[target - num] = i;
    }
  };
  return false;
}

const myNums = [2, 7, 11, 15];
console.log(expectEquals([0, 1], twoSum(myNums, 9)));