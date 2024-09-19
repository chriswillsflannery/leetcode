"""
Maximum Subarray

Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8

Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

"""

from typing import List


class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        """
        approach:
        [2,-3,4,-2,2,1,-1,4]

        compute a max sum seen so far
        and compute a local sum
        if local sum ever dips below 0 reset it
        
        """
                
        maxSum = nums[0]
        localSum = 0

        for num in nums:
            localSum += num
            maxSum = max(maxSum, localSum)
            if localSum < 0:
                localSum = 0
        return maxSum
