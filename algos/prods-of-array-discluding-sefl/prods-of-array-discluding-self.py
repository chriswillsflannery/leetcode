from typing import List

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums)):
            prefix = prefix * nums[i - 1]
            prods[i] = prods[i] * prefix
        
        print(prods)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prods[i] = prods[i] * postfix
            postfix = postfix * nums[i]
        
        print(prods)

        return prods