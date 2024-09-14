"""
given an array of ints and int k, return total number 
of contiguous subarrays whose sum equals k

ex1
input nums = [1,1,1] k=2
output= 2
reason: 1,1 (indeces 0,1) and 1,1 (indeces 1,2)
"""

from typing import List

class Solution:
    def subarray(self, nums: List[int], k: int) -> int:
        # build up array of prefixes
        # for each prefix, get difference between prefix and k
        # is there a breakpoint in the contiguous subarray such that we can 
        # make the prefix == k?

        # build up a hash of prefixSum to count 
        # this accounts for possibility of negative numbers

        # simultaneously build up list of prefixes
        # while we compute our result, so that we're only
        # removing prefixes which are part of the subarray
        #we've seen so far

        # make sure to include an empty prefixSum for 0

        res = 0
        currSum = 0

        prefixSums = { 0: 1 }

        for n in nums:
            currSum += n
            diff = currSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return res


