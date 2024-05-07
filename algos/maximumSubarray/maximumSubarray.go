package maximumsubarray

import "math"

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

func maximumSubarray(nums []int) int {
	// 2 pointer approach
	// find largest max seen so far
	// look at each index and ask, what' the max subarray we've seen at this index?
	// compare each current element against current element plus max subarray ending at previous index

	prevMaxSum := nums[0]
	curSum := 0

	for i := 0; i < len(nums); i++ {
		if curSum < 0 {
			curSum = 0
		}
		curSum += nums[i]
		prevMaxSum = int(math.Max(float64(prevMaxSum), float64(curSum)))
	}

	return prevMaxSum
}