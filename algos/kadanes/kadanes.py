"""
[4,-1,2,-7,3,4]

find a non empty subarray with the largest sum
"""

from typing import List


class Solution:
    def kadanes(self, nums: List[int]) -> int:
        # compute sum so far
        # if local sum ever drops below 0, it won't be useful
        # in computing next largest sum, so we can discard it

        # for example. if we have [4,-1,2,-7, 3, 4]
        # sum 4. then sum 3. then sum 5.
        # then sum -2. (5-7)
        # -2 is not useful to us. We can't use it to compute a next
        # greatest sum, so we can discard it, and reset local sum to 0.
        # but we should remember that 5 was the greatest sum we've
        # seen so far.

        maxSum = nums[0]
        localSum = 0

        for num in nums:
            localSum += num
            maxSum = max(maxSum, localSum)
            if localSum < 0:
                localSum = 0
        return maxSum
    
    def kadanesSlidingWindow(self, nums: List[int]) -> int:
        
