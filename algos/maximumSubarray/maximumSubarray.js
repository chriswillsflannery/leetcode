/*
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
*/

// look at each index and ask, what's the max subarray ending at this index?
// compare each current element against current element combined with maximum subarray ending at previous index

/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
  let prevMaxSum = nums[0]; // 1
  let curSum = 0; // 0
  for (let i = 0; i < nums.length; i++) {
    if (curSum < 0) curSum = 0;
    curSum += nums[i];
    prevMaxSum = Math.max(prevMaxSum, curSum);
  }
  return prevMaxSum;
};

console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])); // 6